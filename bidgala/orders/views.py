# Standard library imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.db import transaction
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime, timezone
import logging
from django.http import JsonResponse
import base64
import sys

# Related third party imports
import stripe
import aftership


# Local application/library specific imports
from . import email_notification_template
from chat.constants import get_decline_message, get_accept_message
from accounts import constants, choices
from products import choices as  product_choices
from chat.models import Conversation, Message
from payments.models import OrderHold, Orders, Stripe
from products.models import Product
from accounts.models import UserInfo
from .models import Inquiry
from payments.utils import create_payment_intent, confirm_payment_intent
from .utils import create_aftership_tracking
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email
from influencer.models import Influencer, InfluencerEarning, AllInfluencerSale

# TODO : Change the helper function name. Also create a different app for emails.


#Helper
def sendEmail(user, product, type, tracking_id="", order_obj=None):
    try:
        is_receipt = False
        customer_name = user.user.first_name + ' ' + user.user.last_name
        from_email = settings.FROM_EMAIL
        to_email = user.user.email
        subject='Order update'

        IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
        data1 = read_image(IMG_1_PATH)

        if type == 'ACCEPT':
            #order_confirmation_receipt(name, phone, address, order_id, date, art_price, shipping, total, tax):
            address = order_obj.order_hold.address + '<br>' + order_obj.order_hold.city + ', ' + order_obj.order_hold.state + '<br>' + order_obj.order_hold.country + '<br>' + order_obj.order_hold.phone
            total = str(order_obj.price)
            order_id = str(order_obj.id) 
            date = str(order_obj.order_hold.accepted_timestamp.date())

            message_ = create_message(to_email, subject, email_notification_template.order_confirmation_receipt(customer_name, product.art_title, address, order_id, date, total))
            is_receipt = True

        elif type == 'DECLINE':
            message_ = create_message(to_email, subject, email_notification_template.orderDeclinedTemplate(customer_name, product.art_title, product.owner.id))
            
        elif type == 'TRACKING':
            
            message_ = create_message(to_email, subject, email_notification_template.trackingNumberTemplate(customer_name, product.art_title, product.owner.id, tracking_id))
            
        attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')

        if not is_receipt:
            message_.add_attachment(attachment1)

        sendgrid_send_email(message_)
        
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))


@login_required
def orders(request):
    """ This method is used to retrive all the order holds that need to be accepted
        for a given user.
    """
    user = UserInfo.objects.get(user = request.user)
    order_hold_obj = OrderHold.objects.filter(seller=user).filter(declined=False).filter(has_tracking=False).order_by('-created_timestamp')
    need_to_accept = []
    for obj in order_hold_obj:
        messages = Message.objects.filter(order_hold=obj).filter(has_input=True).exclude(origin_user=user).order_by('-timestamp')
        if messages.count() > 0:
            need_to_accept.append(messages)
    
    # check if user has stripe activated (maybe move this over to a model method on the UserInfo model so not repeated multiple times)
    seller_stripe_obj, stripe_enabled = user.seller_has_stripe(user)


    order_bought = OrderHold.objects.filter(buyer=user).filter(accepted=True).order_by('-accepted_timestamp').values('id')
    orders = Orders.objects.filter(Q(order_hold__in=order_bought))

    purchase_pending = OrderHold.objects.filter(buyer=user).filter(declined=False, accepted=False).order_by('-declined_timestamp')
    

    seller_order_accepted = OrderHold.objects.filter(seller=user).filter(accepted=True).order_by('-accepted_timestamp')
    
    context = {
    'pendings' : need_to_accept,
    'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
    'has_elements' : True if len(need_to_accept) > 0 else False,
    'category' : product_choices.category,
    'bought' : orders,
    'purchase_pending' : purchase_pending,
    
    'seller_order_accepted' : seller_order_accepted, 
    'stripe_enabled': stripe_enabled
    }
    
    return render(request, 'orders/orders.html', context)



@login_required
def accepted_orders(request):
    user = UserInfo.objects.get(user = request.user)
    order_hold_obj = OrderHold.objects.filter(seller=user).filter(has_tracking=True)
    accepted = []
    for obj in order_hold_obj:
        messages = Message.objects.filter(order_hold=obj).filter(has_input=True).exclude(origin_user=user).order_by('timestamp')
        if messages.count() > 0:
            accepted.append(messages)

    context = {
    'accepted' : accepted,
    'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
    'has_elements' : True if len(accepted) > 0 else False,
    'category' : product_choices.category
    }
    
    return render(request, 'orders/orders.html', context)


@login_required
def declined_orders(request):
    user = UserInfo.objects.get(user = request.user)
    order_hold_obj = OrderHold.objects.filter(seller=user).filter(has_tracking=False).filter(declined=True)
    declined = []
    for obj in order_hold_obj:
        messages = Message.objects.filter(order_hold=obj).filter(has_input=True).exclude(origin_user=user).order_by('timestamp')
        if messages.count() > 0:
            declined.append(messages)

    context = {
    'declined' : declined,
    'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
    'has_elements' : True if len(declined) > 0 else False,
    'category' : product_choices.category
    }
    
    return render(request, 'orders/orders.html', context)


@login_required
def purchased_orders(request):
    user = UserInfo.objects.get(user = request.user)
    order_hold_obj = OrderHold.objects.filter(buyer=user).filter(accepted=True)

    context = {
    'purchases' : order_hold_obj,
    'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
    'category' : product_choices.category
    }
    seller_stripe_obj = None
    return seller_stripe_obj, stripe_enabled


@login_required
def accept_or_decline_order(request):
    """ This method is used to accept the order request for a product whose
        id is passed in the POST request.
    """
    try:
        if request.method == 'POST':
            # check if request user has stripe/sseller_user.eller
            seller_user = UserInfo.objects.get(user=request.user)
            seller_stripe_obj, stripe_enabled = seller_user.seller_has_stripe(seller_user)

            if stripe_enabled == True:

                validate_tracking = False

                if messages is not None:
                    clear_messages = messages.get_messages(request)
                    if clear_messages:
                        for message in clear_messages:
                            pass

                # if request.POST['submission'] == 'ACCEPT' and len(request.POST.get('tracking_id', '').strip()) < 1:
                # 	messages.error(request, 'Please provide tracking number')
                # 	return redirect(reverse('orders'))

                with transaction.atomic():
                    order_hold_obj = OrderHold.objects.filter(id=request.POST['order_hold'])
                    if order_hold_obj.count() > 0:
                        if request.POST['submission'] == 'DECLINE':
                            with transaction.atomic():
                                order_hold_obj = order_hold_obj.first()
                                order_hold_obj.declined = True
                                order_hold_obj.accepted = False
                                order_hold_obj.declined_timestamp = datetime.now()
                                order_hold_obj.save()

                                msg_obj = Message.objects.filter(order_hold=order_hold_obj).first()
                                msg_obj.has_input = False
                                msg_obj.save()

                                msg_text_decline = get_decline_message(order_hold_obj.product.art_title, order_hold_obj.product.id)
                                decline_message = Message(message_text=msg_text_decline, conversation_id=msg_obj.conversation_id, origin_user=order_hold_obj.seller)
                                decline_message.save()
                                messages.success(request, 'Rejected buyer request')

                                ## 
                                # Send Decline email to buyer
                                sendEmail(order_hold_obj.buyer, order_hold_obj.product, 'DECLINE')
                            ##

                        elif request.POST['submission'] == 'ACCEPT':
                            with transaction.atomic():
                                order_hold_obj = order_hold_obj.first()
                                order_hold_obj.accepted = True
                                order_hold_obj.declined = False
                                order_hold_obj.accepted_timestamp = datetime.now()
                                order_hold_obj.save()


 
                                # pass discount code here - final discount code validation happens in create_payment_intent method
                                payment_intent = create_payment_intent(order_hold_obj.customer_stripe_id, seller_stripe_obj.stripe_account_id, order_hold_obj, seller_stripe_obj, order_hold_obj.customer_payment_method_id, order_hold_obj.discount_code)
 

                                order_hold_obj.payment_intent = payment_intent.id
                                order_hold_obj.save()


                                
                                orders_obj = Orders(order_date=datetime.now(),customer_stripe_id=order_hold_obj.customer_stripe_id, \
                                    order_hold=order_hold_obj, price=order_hold_obj.amount_total, seller_connect_acc_id=seller_stripe_obj.stripe_account_id, payment_intent=payment_intent.id, )
                                orders_obj.save()

                                product_obj = Product.objects.get(id=order_hold_obj.product.id)
                                product_obj.sold = True
                                product_obj.save()

                                msg_obj = Message.objects.filter(order_hold=order_hold_obj).first()

                                msg_text_accepted = get_accept_message(order_hold_obj.buyer, order_hold_obj.product)
                                accept_message = Message(message_text=msg_text_accepted, conversation_id=msg_obj.conversation_id, origin_user=order_hold_obj.seller)
                                accept_message.save()
                                messages.success(request, 'Request accepted')

                                ## 
                                # Send accept email to buyer
                                sendEmail(order_hold_obj.buyer, order_hold_obj.product, 'ACCEPT', order_obj=orders_obj)
                            ##

                        else:
                            messages.error(request, 'Invalid request.')
                            return redirect(reverse('orders'))
                    else:
                        messages.error(request, 'The buyer request does not exists.')
                        return redirect(reverse('orders'))
            else: 
                messages.error(request, 'You cannot accept this request untill you set up stripe')
                return redirect(reverse('orders'))

    except AssertionError as e:
        messages.error(request, 'Something went wrong. Please try later.')
        logging.getLogger("error_logger").error(str(e))

    return redirect(reverse('orders'))

@login_required
def submit_tracking(request):
    if request.method == 'POST':
        tracking_object_created = False
        try:
            if messages is not None:
                clear_messages = messages.get_messages(request)
                if clear_messages:
                    for message in clear_messages:
                        pass
            with transaction.atomic():
                tracking_number = request.POST['tracking_id'].strip()
                product_id = request.POST['product_id'].strip()

                order_hold_obj = OrderHold.objects.get(id=request.POST['order_hold'])

                # Get specific order from Order table with product id (there should only be one order per product in the product table)
                product_order = Orders.objects.get(order_hold=order_hold_obj)
                
                ####
                #Decline tracking submission if it has been submitted 7 days earlier 
                current_time = datetime.now(tz=timezone.utc)
                date_diff_order = current_time - product_order.order_date
                if date_diff_order.days > 7:
                    ord_hld = product_order.order_hold
                    ord_hld.accepted = False
                    ord_hld.declined = True
                    ord_hld.declined_timestamp = datetime.now(tz=timezone.utc)
                    ord_hld.save()
                    product_in_hold = product_order.order_hold.product
                    product_in_hold.available = True
                    product_in_hold.sold = False
                    product_in_hold.save()
                    product_order.delete()
                    messages.error(request, 'Order is automatically declined if tracking number is not provided within 7 days after accepting request.')
                    return redirect(reverse('orders'))
                ####

                if str(product_id) != str(order_hold_obj.product.id):
                    messages.error(request, 'Products match is not found.')
                    return redirect(reverse('orders'))
                # Create tracking and get the tracking id
                aftership_tracking_id = create_aftership_tracking(tracking_number)
                tracking_object_created = True
                # Save tracking number and tracking number id 
                product_order.tracking_number = tracking_number
                product_order.aftership_tracking_id = aftership_tracking_id
                product_order.purchased = True
                product_order.save()

                order_hold_obj.has_tracking = True
                order_hold_obj.save()
 
                if order_hold_obj.influencer:
                    ## Influencer code
                    influencer_obj = order_hold_obj.influencer
                    all_influencer_obj = AllInfluencerSale(influencer=influencer_obj, product=order_hold_obj.product, buyer=order_hold_obj.buyer, seller=order_hold_obj.seller, commission=influencer_obj.commission)
                    all_influencer_obj.save()

                    if not (InfluencerEarning.objects.filter(influencer=influencer_obj).count() > 0):
                        temp_ie = InfluencerEarning(influencer=influencer_obj)
                        temp_ie.save()

                    influencer_earning_obj = InfluencerEarning.objects.filter(influencer=influencer_obj)[0]
                    influencer_earning_obj.total_amount = influencer_earning_obj.total_amount + order_hold_obj.amount_total 
                    influencer_earning_obj.commission_owned = influencer_earning_obj.commission_owned + order_hold_obj.amount_total 
                    influencer_earning_obj.total_prices = influencer_earning_obj.total_prices + order_hold_obj.product.price
                    influencer_earning_obj.total_shippings = influencer_earning_obj.total_shippings + order_hold_obj.shipping_price
                    influencer_earning_obj.total_sales = influencer_earning_obj.total_sales + 1
                    influencer_earning_obj.commission_earned = influencer_earning_obj.commission_earned + (order_hold_obj.amount_total * influencer_obj.commission)
                    influencer_earning_obj.save()
                    ####



                msg_obj = Message.objects.filter(order_hold=order_hold_obj).first()

                confirm_payment_intent(product_order.payment_intent, order_hold_obj, product_order)
                tracking_message = Message(message_text='Tracking Number : <a style="color:#0275d8" href="https://rockmyworldaa8q.aftership.com/'+tracking_number+'">' + tracking_number + '</a>' , conversation_id=msg_obj.conversation_id, origin_user=order_hold_obj.seller)
                tracking_message.save()
                sendEmail(order_hold_obj.buyer, order_hold_obj.product, 'TRACKING', tracking_id=tracking_number)
                messages.success(request, 'Tracking number submitted.')

                return redirect(reverse('orders'))

        except Exception as e:
            logging.getLogger("error_logger").error('Error on line {}'.format(sys.exc_info()[-1].tb_lineno) + ' ' + str(e))
            if messages is not None:
                clear_messages = messages.get_messages(request)
                if clear_messages:
                    for message in clear_messages:
                        pass
            if tracking_object_created:
                try:
                    tracking_id = request.POST['tracking_id'].strip()
                    aftership.tracking.delete_tracking(tracking_id=tracking_id)
                except aftership.exception.NotFound:
                    None    
            
            messages.error(request, 'Something went wrong. Please try again later or enter a valid tracking number.')
            return redirect(reverse('orders'))
    else:
        messages.error(request, 'Request Failed.')
        return redirect(reverse('orders'))		


@login_required
def inquiry(request):
    status_code = None
    try:
        if request.method == 'POST':
            if len(request.POST['first_name_popup'].strip()) > 0 and \
                len(request.POST['last_name_popup'].strip()) > 0 and \
                len(request.POST['address_popup'].strip()) > 0 and \
                len(request.POST['postal_popup'].strip()) > 0 and \
                len(request.POST['city_popup'].strip()) > 0 and \
                len(request.POST['state_popup'].strip()) > 0 and \
                len(request.POST['country'].strip()) > 0 and \
                len(request.POST['phone_popup'].strip()) > 0 and \
                len(request.POST['product_id'].strip()) > 0 :

                
                product_obj = Product.objects.get(id=request.POST['product_id'].strip())
                user_info_obj = UserInfo.objects.get(user=request.user)

                inquiry_obj = Inquiry(user=user_info_obj,
                                      product = product_obj,
                                      first_name = request.POST['first_name_popup'].strip(),
                                      last_name = request.POST['last_name_popup'].strip(),
                                      address = request.POST['address_popup'].strip(),
                                      apt_number = request.POST['apt_popup'].strip(),
                                      postal_code = request.POST['postal_popup'].strip(),
                                      city = request.POST['city_popup'].strip(),
                                      state = request.POST['state_popup'].strip(),
                                      country = request.POST['country'].strip(),
                                      phone = request.POST['phone_popup'].strip()
                                    )
                inquiry_obj.save()

                response = {
                    'status' : 'success',
                    'message' : 'Inquiry submitted',
                }
                status_code = 200

    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
        response = {
                    'status' : 'fail',
                    'message' : 'Inquiry unsuccessful. Please try again later.',
                }
        status_code = 500
        
    return JsonResponse(response, status=status_code)
    
@staff_member_required
def inquiry_delete(request):
    try:
        if request.method == 'POST':
            user_id = request.POST['user']	
            product_id = request.POST['product']
            
            product_obj = Product.objects.filter(id=product_id).first()
            user_info_obj = UserInfo.objects.get(id=user_id)
            inquiry_obj = Inquiry.objects.filter(product=product_obj).filter(user=user_info_obj)[0]
            inquiry_obj.delete()

            # TODO Need email for rejections

    except Exception as e:
        
        logging.getLogger("error_logger").error(str(e))
    
    return redirect(request.META.get('HTTP_REFERER'))

@staff_member_required
def inquiry_accept(request):
    try:
        if request.method == 'POST':
            user_id = request.POST['user']
            product_id = request.POST['product']
            
            with transaction.atomic():

                product_obj = Product.objects.filter(id=product_id).first()

                user_info_obj = UserInfo.objects.get(id=user_id)

                inquiry_obj = Inquiry.objects.filter(product=product_obj).filter(user=user_info_obj)[0]

                total_price = None
                shipping_price = None
                product_price = inquiry_obj.product.price


                if inquiry_obj.country.lower() == 'canada':
                    shipping_price = product_obj.shipping_price_can

                elif inquiry_obj.country.lower() == 'united states':
                    shipping_price = product_obj.shipping_price_us

                elif inquiry_obj.country.lower() == 'uk':
                    shipping_price = product_obj.shipping_price_uk

                elif inquiry_obj.country.lower() == 'asia': 
                    shipping_price = product_obj.shipping_price_asia

                elif inquiry_obj.country.lower() == 'australia': 
                    shipping_price = product_obj.shipping_price_aunz

                elif inquiry_obj.country.lower() == 'new zealand': 
                    shipping_price = product_obj.shipping_price_aunz

                elif inquiry_obj.country.lower() == 'europe': 
                    shipping_price = product_obj.shipping_price_europe

                elif inquiry_obj.country.lower() == 'other': 
                    shipping_price = product_obj.shipping_price_other

                
                total_price = int(shipping_price) + int(product_price)

                if not product_obj.sold:
                    order_hold_obj = OrderHold(product=product_obj, buyer=user_info_obj, seller=product_obj.owner, first_name=inquiry_obj.first_name, last_name=inquiry_obj.last_name, phone=inquiry_obj.phone, address=inquiry_obj.address, city=inquiry_obj.city, state=inquiry_obj.state, zip=inquiry_obj.postal_code, apt=inquiry_obj.apt_number, country=inquiry_obj.country, amount_total=total_price, amount_subtotal=total_price, shipping_price=shipping_price, accepted=True, accepted_timestamp=datetime.now(tz=timezone.utc))
                    order_hold_obj.save()

                    orders_obj = Orders(order_date=datetime.now(), order_hold=order_hold_obj, price=order_hold_obj.amount_total, purchased=True)
                    orders_obj.save()

                    product_obj.sold = True
                    product_obj.save()

                    inquiry_obj.accepted = True
                    inquiry_obj.save()

                    inquiry_obj = Inquiry.objects.filter(product=product_obj).filter(accepted=False)
                    inquiry_obj.delete()
                
         
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
    
    return redirect(request.META.get('HTTP_REFERER'))