from django.db import models
from datetime import datetime
import uuid

from accounts.models import UserInfo
from products.models import Product
from influencer.models import Influencer

# Create your models here.
class Stripe(models.Model):
	user = models.ForeignKey(UserInfo, null=True, on_delete=models.DO_NOTHING)
	stripe_account_id = models.CharField(blank=True, max_length=200)
	access_token = models.CharField(blank=True, max_length=200)
	stripe_publishable_key = models.CharField(blank=True, max_length=200)
	added_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.user.user.email
	
class OrderHold(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(null=True, max_length=20)
	last_name = models.CharField(null=True, max_length=20)
	phone = models.CharField(null=True, max_length=15)
	address = models.CharField(null=True, max_length=150)
	city = models.CharField(null=True, max_length=20)
	state = models.CharField(null=True, max_length=20)
	country = models.CharField(null=True, max_length=20)
	zip = models.CharField(null=True, max_length=10)
	apt = models.CharField(null=True, max_length=10)
	amount_total = models.IntegerField(null=True)
	amount_subtotal = models.IntegerField(null=True)
	currency = models.CharField(null=True, max_length=5)
	tax = models.IntegerField(null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True)
	buyer = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='buyer')
	seller = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='seller')
	created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
	accepted = models.BooleanField(blank=False, default=False)
	declined = models.BooleanField(blank=False, default=False) 
	has_tracking = models.BooleanField(blank=False, default=False) 
	accepted_timestamp = models.DateTimeField(null=True)
	declined_timestamp = models.DateTimeField(null=True)
	checkout_token =  models.CharField(blank=True, max_length=200)
	payment_intent = models.CharField(blank=True, max_length=200)
	shipping_price = models.IntegerField(null=True)
	discount_code =	models.CharField(blank=True, max_length=200)
	influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, null=True)


	customer_stripe_id = models.CharField(blank=True, max_length=200)
	customer_payment_method_id = models.CharField(blank=True, max_length=200)

	def __str__(self):
 		return str(self.id) 


class Orders(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	order_date = models.DateTimeField(default=datetime.now, blank=True)
	purchased = models.BooleanField(blank=False, default=False) 
	tracking_number = models.CharField(blank=True, max_length=200)
	aftership_tracking_id = models.CharField(blank=True, max_length=200)
	courier_company = models.CharField(blank=True, max_length=50)
	shipping_to = models.CharField(blank=True, max_length=20)
	price = models.IntegerField(blank=False, default=0)
	checkout_token =  models.CharField(blank=True, max_length=200)
	payment_intent = models.CharField(blank=True, max_length=200)
	order_hold = models.ForeignKey(OrderHold, on_delete=models.CASCADE, related_name='orderhold', null=True)

	seller_connect_acc_id = models.CharField(blank=True, max_length=200)
	cloned_customer_id = models.CharField(blank=True, max_length=200)

	customer_stripe_id = models.CharField(blank=True, max_length=200)

	def __str__(self):
 		return str(self.id)