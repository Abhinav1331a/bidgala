# Standard library imports
import urllib
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from datetime import datetime, timezone, timedelta
import json
import logging



# Related third party imports
import stripe
import aftership

# Local application/library specific imports
from accounts import constants, choices
from accounts.models import UserInfo
from .models import Stripe, Orders, OrderHold
from products.models import Product
from chat.constants import get_purchase_message, get_buyer_message
from chat.models import Conversation, Message
from .utils import create_account_link, get_or_create_customer
from . import email_template
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email
from influencer.models import Influencer

# Seller Stripe account onboarding
@login_required
def onboard_seller(request):

    if request.user.is_authenticated:
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            user = UserInfo.objects.get(user=request.user)
            if Stripe.objects.filter(user=user).count() > 0:
                stripe_acc = Stripe.objects.get(user=user)
                stripe_acc_id = stripe_acc.stripe_account_id

                temp_account, onboarding_complete = user.stripe_onboarding_status_info(stripe_acc_id)

                if onboarding_complete is False:
                    link_obj = create_account_link(stripe_acc_id)
                    onboarding_url = link_obj.url
                    return redirect(onboarding_url)
                else:
                    return redirect('profile')
            else:
                account = stripe.Account.create(
                    type='standard',
                    email=request.user.email,
                    business_profile={
                        'name': request.user.first_name + " " + request.user.last_name + " " + "Art"
                    }
                )
                Stripe.objects.create(stripe_account_id=account.id, user=user)

                link_obj = create_account_link(account)
                onboarding_url = link_obj.url
                return redirect(onboarding_url)
        except Exception as e:
            logging.getLogger("error_logger").error(str(e))
            return redirect('profile')
    else:
        return redirect('login')


@login_required
def purchase_transition(request):
    if '/art/product_view/' in request.META.get('HTTP_REFERER'):
        context = {}
        context['chat'] = request.GET.get('chat', '')
        try:
            product_obj = Product.objects.filter(id=request.GET.get('product', ''))[0]
            order_obj = OrderHold.objects.filter(product=product_obj)[0]
            context['order'] = order_obj
        except Exception as e:
            logging.getLogger("error_logger").error(str(e))
        return render(request, 'pages/purchase_transition.html', context)
    else:
        return redirect('index')

@login_required
def apply_discount(request):
    if request.method == "POST":
        discount_code = json.loads(request.body)
        discount = constants.LAUNCH_DISCOUNT
        if (discount_code == constants.LAUNCH_DISCOUNT_CODE):
            customer = UserInfo.objects.get(user=request.user)
            if (customer.is_professional and customer.company_email_verified):
                return JsonResponse({'status': 'fail', 'message' : 'You already have a discount applied'})
            elif (customer.first_buy == False):

                return JsonResponse({'status': 'success', 'message' : 'Discount applied!', 'discount': discount})
            else:
                return JsonResponse({'status': 'fail', 'message' : 'You are not eligible to redeem this discount. This discount can only be applied to your first purchase.'})

        ## This condition is used for influencer coupon
        elif Influencer.objects.filter(coupon__iexact=discount_code).count() == 1:
            discount = Influencer.objects.filter(coupon__iexact=discount_code)[0].discount
            return JsonResponse({'status': 'success', 'message' : 'Discount applied!', 'discount': discount})
        else:
            return JsonResponse({'status': 'fail', 'message' : 'Discount code does not exist'})



# Payment flow
@login_required
def submit_purchase_request(request):
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        customer = request.user
        json_data = json.loads(request.body)

        product_and_shipping = json_data['amount']
        shipping_price = json_data['shipping_price']
        product_id = json_data['product_id']

        buyer_cus_stripe_id = json_data['customer_stripe_id']
        stripe_payment_method_id = json_data['payment_method_id']
        buyer_first_name = json_data['first_name']
        buyer_last_name = json_data['last_name']
        buyer_phone = json_data['phone']
        buyer_address = json_data['address']
        buyer_city = json_data['city']
        buyer_state = json_data['state']
        buyer_postal = json_data['zip']
        buyer_apt = json_data['apt']
        discount_code = json_data['discount_code']
        has_influencer = False
        influencer_obj = None

        # still need to add country

        try:
            with transaction.atomic():
                product = Product.objects.filter(id=product_id).first()

                if product.owner.user == request.user:
                    return JsonResponse({'status': 'fail', 'message' : 'Artist and Buyer cannot be same'}, status=500)

                buyer = UserInfo.objects.get(user=customer)
                check_prev_hold = OrderHold.objects.filter(product_id=product.id, buyer=buyer).order_by('-created_timestamp')

                if check_prev_hold.count() > 0:
                    date_diff = datetime.now(timezone.utc) - check_prev_hold.first().created_timestamp

                    if date_diff.days <= 7:
                        if not check_prev_hold.first().declined:
                            return JsonResponse({'status': 'fail', 'message' : 'You already requested for this item. Please wait for the artist confirmation or send a message to artist in chat'}, status=500)

                if product.sold:
                    return JsonResponse({'status': 'fail', 'message' : 'This item is already sold.'}, status=500)

                # validate discount code if exists
                if discount_code == constants.LAUNCH_DISCOUNT_CODE or discount_code == "":
                    if buyer.is_professional and buyer.company_email_verified and len(discount_code) > 0:
                        discount_code = None
                        return JsonResponse({'status': 'fail', 'message' : 'You already have a discount applied'}, status=500)
                    elif buyer.first_buy == False:
                        discount_code = json_data['discount_code']
                    elif buyer.first_buy == True and discount_code == constants.LAUNCH_DISCOUNT_CODE:
                        discount_code = None
                        return JsonResponse({'status': 'fail', 'message' : 'You are not eligible to redeem this discount. This discount can only be applied to your first purchase.'}, status=500)

                ## Influencer code here
                elif Influencer.objects.filter(coupon__iexact=discount_code).count() == 1:
                    if buyer.is_professional and buyer.company_email_verified:
                        discount_code = None
                        return JsonResponse({'status': 'fail', 'message' : 'You already have a discount applied'}, status=500)
                    else:
                         discount_code = json_data['discount_code']
                         has_influencer = True

                ## endof influencer code
                else: 
                    discount_code = None
                    return JsonResponse({'status': 'fail', 'message' : 'Discount code does not exist'}, status=500)


                country = json_data['shipping_country'].strip()
                state = json_data['state']
                shipping_price = json_data['shipping_price']

                region = json_data['region'].strip()

                # Actual data in db
                actual_price = product.price
                actual_shipping_price = 0

                if not (country in choices.stripe_shipping_support[region]):
                    return JsonResponse({'status': 'fail', 'message': 'country is not in this region'}, status=500)


                if region == 'US' and product.show_shipping_price_us:
                    actual_shipping_price = product.shipping_price_us

                elif region == 'CANADA' and product.show_shipping_price_can:
                    actual_shipping_price = product.shipping_price_can

                elif region == 'UK' and product.show_shipping_price_uk:
                    actual_shipping_price = product.shipping_price_uk

                elif region == 'ASIA' and product.show_shipping_price_asia:
                    actual_shipping_price = product.shipping_price_asia

                elif region == 'AUSTRALIA/NEW ZEALAND' and product.show_shipping_price_aunz:
                    actual_shipping_price = product.shipping_price_aunz

                elif region == 'EUROPE' and product.show_shipping_price_europe:
                    actual_shipping_price = product.shipping_price_europe

                elif region == 'OTHER' and product.show_shipping_price_other:
                    actual_shipping_price = product.shipping_price_other

                subtract_discount = 0
                current_user = UserInfo.objects.get(user=request.user)
                professional_verified = True if (current_user.is_professional and current_user.company_email_verified) else False

                if professional_verified:
                    subtract_discount = actual_price * constants.PROFESSIONAL_DISCOUNT



                if (actual_price - subtract_discount + actual_shipping_price) != float(product_and_shipping):
                    return JsonResponse({'status': 'failed', 'message': 'price not matched'}, status=500)

                conversation_obj, created = Conversation.objects.get_or_create(buyer.user, product.owner.id)


                if not has_influencer:
                    hold_obj = OrderHold(product=product, buyer=buyer, seller=product.owner, first_name=buyer_first_name, last_name=buyer_last_name, phone=buyer_phone, address=buyer_address, city=buyer_city, state=buyer_state, zip=buyer_postal, apt=buyer_apt, country=country, amount_total=product_and_shipping, amount_subtotal=product_and_shipping, customer_stripe_id=buyer_cus_stripe_id, customer_payment_method_id=stripe_payment_method_id, shipping_price=int(shipping_price), discount_code=discount_code)
                else:
                    influencer_obj = Influencer.objects.filter(coupon__iexact=discount_code)[0]
                    hold_obj = OrderHold(product=product, buyer=buyer, seller=product.owner, first_name=buyer_first_name, last_name=buyer_last_name, phone=buyer_phone, address=buyer_address, city=buyer_city, state=buyer_state, zip=buyer_postal, apt=buyer_apt, country=country, amount_total=product_and_shipping, amount_subtotal=product_and_shipping, customer_stripe_id=buyer_cus_stripe_id, customer_payment_method_id=stripe_payment_method_id, shipping_price=int(shipping_price), discount_code=discount_code, influencer=influencer_obj)
                # if hold_obj.buyer.first_buy == False:
                #     hold_obj.buyer.first_buy = Truete

                hold_obj.save()

                msg_text_seller = get_purchase_message(buyer, product)
                msg_text_buyer = get_buyer_message(product.art_title, product.id)
                msg_buyer = Message(message_text=msg_text_buyer, conversation_id=conversation_obj, origin_user=buyer, has_input=True, order_hold=hold_obj)
                msg_owner = Message(message_text=msg_text_seller, conversation_id=conversation_obj, origin_user=product.owner, buyer_notify_msg=True)
                msg_buyer.save()
                msg_owner.save()

                try:
                    artist_name = product.owner.user.first_name if product.owner.user.first_name  else 'Artist'
                    buyer_name = buyer.user.first_name if buyer.user.first_name else buyer.user.username

                    to_email = product.owner.user.email
                    subject = 'Purchase request'

                    IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
                    data1 = read_image(IMG_1_PATH)
                    IMG_facebook_PATH = settings.BASE_DIR + '/bidgala/static/img/email/facebook.png'
                    data_facebook = read_image(IMG_facebook_PATH)
                    IMG_twitter_PATH = settings.BASE_DIR + '/bidgala/static/img/email/twitter.png'
                    data_twitter = read_image(IMG_twitter_PATH)
                    IMG_instagram_PATH = settings.BASE_DIR + '/bidgala/static/img/email/instagram.png'
                    data_instagram = read_image(IMG_instagram_PATH)
                    IMG_linkedin_PATH = settings.BASE_DIR + '/bidgala/static/img/email/linkedin.png'
                    data_linkedin = read_image(IMG_linkedin_PATH)
                    IMG_pinterest_PATH = settings.BASE_DIR + '/bidgala/static/img/email/pinterest.png'
                    data_pinterest = read_image(IMG_pinterest_PATH)

                    message_ = create_message(to_email, subject, email_template.acceptRequest(artist_name, buyer_name, product))

                    attachment1 = create_attachment(data1, 'img/jpg', 'logo.jpg', 'logo')
                    attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
                    attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
                    attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
                    attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
                    attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')

                    message_.add_attachment(attachment1)
                    message_.add_attachment(attachment_facebook)
                    message_.add_attachment(attachment_twitter)
                    message_.add_attachment(attachment_instagram)
                    message_.add_attachment(attachment_linkedin)
                    message_.add_attachment(attachment_pinterest)
                    try:
                       sendgrid_send_email(message_)
                    except Exception as e:
                        logging.getLogger("error_logger").error(str(e))

                except Exception as e:
                    logging.getLogger("error_logger").error(str(e))


                return JsonResponse({'status': 'success', 'message' : 'Your purchase request was submitted successfully', 'seller_chat': product.owner.id})

        except Exception as e:
            logging.getLogger("error_logger").error(str(e))
            raise Exception(e)

@login_required
def add_payment_method(request):
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        buyer = request.user
        json_data = json.loads(request.body)

        product_id = json_data['product_id']
        try:
            with transaction.atomic():
                stripe_customer = get_or_create_customer(buyer)

                session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        mode='setup',
                        customer=stripe_customer,
                        success_url= settings.HOST_BASE_URL + "art/product_view/" + product_id + "?modal=open&status=success",
                        cancel_url=settings.HOST_BASE_URL + "art/product_view/" + product_id + "?modal=open",
                        metadata={'bidgala_user': buyer},
                        billing_address_collection='required'
                    )

                if session:
                    return JsonResponse({'sessionId': session['id']})
                else:
                    return JsonResponse({'status': 'fail', 'message' : 'unable to create a payment session.'}, status=500)

        except stripe.error.CardError as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

        except stripe.error.RateLimitError as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

        except stripe.error.InvalidRequestError as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

        except stripe.error.AuthenticationError as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

        except stripe.error.APIConnectionError as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

        except stripe.error.StripeError as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

        except Exception as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail'}, status=500)

@login_required
def delete_payment_method(request):
    if request.method == "POST":
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            json_data = json.loads(request.body)

            payment_method = json_data['payment_method_id']

            if OrderHold.objects.filter(customer_payment_method_id=payment_method).count() > 1:
                return JsonResponse({'status': 'fail', 'message': 'You cannot delete this payment method at this time because it is associated with an incomplete order you placed.', 'pm_id': payment_method}, status=500)

            else:
                stripe.PaymentMethod.detach(
                    payment_method
                )

                return JsonResponse({'status': 'success', 'message': 'payment method removed successfully', 'pm_id': payment_method})
        except Exception as e:
            logging.getLogger("error_logger").error(str(e))
            return JsonResponse({'status': 'fail', 'message' : 'unable to remove payment method'}, status=500)


# TODO
# Stripe webhook functions - need to have a new one to see when a user disconnects from stripe and we can delete their stripe info from our db
# @csrf_exempt
# def check_checkout_status_webhook(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#         payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
#         )
#         session = event['data']['object']

#         if event['type'] == 'checkout.session.completed':
#             create_hold_and_message(session)

#         elif event['type'] == 'charge.expired':
#             trigger_expired_holds(session)

#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)
#     except Exception as e:
#         return HttpResponse(status=400)

#     # Passed signature verification
#     return HttpResponse(status=200)
