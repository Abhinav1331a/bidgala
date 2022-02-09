from django.conf import settings

import sys
import stripe 
import logging
from accounts.models import UserInfo
from accounts import constants
from influencer.models import Influencer



def calculate_application_fee(shipping, price, buyer, discount_code):
    if buyer.is_professional == True and buyer.company_email_verified == True:
        credit = price * constants.PROFESSIONAL_DISCOUNT
        final_amount = ((price - credit) + shipping)

        application_fee = (((price * (constants.COMMISION - constants.PROFESSIONAL_DISCOUNT))) + (shipping * constants.COMMISION))
        # min app fee for future discounts

        return application_fee, final_amount

    elif discount_code == constants.LAUNCH_DISCOUNT_CODE and buyer.is_professional != True and buyer.company_email_verified != True:
        credit = price * constants.LAUNCH_DISCOUNT
        final_amount = ((price - credit) + shipping)

        application_fee = (((price * (constants.COMMISION - constants.LAUNCH_DISCOUNT))) + (shipping * constants.COMMISION))
        # min app fee for future discounts

        return application_fee, final_amount
    
    elif Influencer.objects.filter(coupon__iexact = discount_code).count() == 1:
        influencer_discount = Influencer.objects.filter(coupon__iexact = discount_code)[0].discount
        credit = price * influencer_discount
        final_amount = ((price - credit) + shipping)
        application_fee = (((price * (constants.COMMISION - influencer_discount))) + (shipping * constants.COMMISION))
        return application_fee, final_amount

    else:
        final_amount = shipping + price
        application_fee = ((final_amount * (constants.COMMISION)))
        
        return application_fee, final_amount


def clone_connect_payment_method(customer, connect_id, payment_method):
	stripe.api_key = settings.STRIPE_SECRET_KEY

	payment_method = stripe.PaymentMethod.create(
		payment_method=payment_method,
		stripe_account=connect_id,
		customer=customer,
	)

	return payment_method.id


def create_payment_intent(customer, connect_acc, order_hold, seller_stripe, customer_pm, discount_code):
	try:
		stripe.api_key = settings.STRIPE_SECRET_KEY

		payment_method = clone_connect_payment_method(customer, connect_acc, customer_pm)

		product_price = order_hold.product.price
		buyer = order_hold.buyer
		shipping_price = order_hold.shipping_price

		stripe_connect_acc = seller_stripe.stripe_account_id

		(application_fee, final_amount) = calculate_application_fee(shipping_price, product_price, buyer, discount_code)

		payment_intent = stripe.PaymentIntent.create(
			amount=int(final_amount*100),
			currency='usd',
			application_fee_amount=int(application_fee*100),
			stripe_account=stripe_connect_acc,
			payment_method=payment_method, 
		)

		return payment_intent

	except Exception as e:
		logging.getLogger("error_logger").error('Error on line {}'.format(sys.exc_info()[-1].tb_lineno) + ' ' + str(e))


def create_account_link(stripe_account):
    account_link = stripe.AccountLink.create(
        account=stripe_account,
        refresh_url= settings.HOST_BASE_URL + 'payments/reauth',
        return_url= settings.HOST_BASE_URL + 'settings',
        type='account_onboarding',
    )

    return account_link


def get_or_create_customer(buyer):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    current_user = UserInfo.objects.get(user=buyer)

    if current_user.stripe_customer_id:
        stripe_customer = current_user.stripe_customer_id

    else:
        customer = stripe.Customer.create(
            email=buyer.email,
            name=buyer.first_name + " " + buyer.last_name,
        )

        stripe_customer = customer.id

        current_user.stripe_customer_id = stripe_customer
        current_user.save()

    return stripe_customer


def confirm_payment_intent(payment_intent, order_hold_obj, order_obj):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    stripe.PaymentIntent.confirm(
        payment_intent,
        stripe_account=order_obj.seller_connect_acc_id,
        receipt_email=order_hold_obj.buyer.user.email,
        off_session='true',
        shipping={
            'address':  {
                'line1': order_hold_obj.address,
                'city': order_hold_obj.city,
                'country': order_hold_obj.country,
                'line2': order_hold_obj.apt,
                'postal_code': order_hold_obj.zip,
                'state': order_hold_obj.state
            },
            'name': order_hold_obj.first_name + " " + order_hold_obj.last_name,
            'phone': order_hold_obj.phone,
            'tracking_number': order_obj.tracking_number
        }
    )