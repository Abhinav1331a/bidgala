from django.urls import path, include
from . import views

urlpatterns = [
	path('submit-purchase-request', views.submit_purchase_request, name='submit_purchase_request'),
	path('add-payment-method', views.add_payment_method, name='add_payment_method'),
	path('apply-discount', views.apply_discount, name='apply_discount'),
	path('onboard-seller', views.onboard_seller, name='onboard_seller'),
	path('reauth', views.onboard_seller, name='onboard_seller'),
	path('remove-payment-method', views.delete_payment_method, name='remove_payment_method'),
	path('purchase-request-successful', views.purchase_transition, name="purchase_request_successful"),
	# will need this later not in use now
	# path('checkout-status-webhook', views.check_checkout_status_webhook, name='check_checkout_status_webhook'),
]