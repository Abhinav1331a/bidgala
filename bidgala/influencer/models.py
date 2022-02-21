from django.db import models
from datetime import datetime
from django.utils.html import mark_safe
import uuid

from products.models import Product
from accounts.models import UserInfo


class Influencer(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=20, null=False, blank=False)
	last_name = models.CharField(max_length=20, null=True)
	instagram = models.CharField(max_length=60, null=True)
	email = models.CharField(max_length=50, blank=False, null=False)
	phone = models.CharField(max_length=20, blank=False, null=False)
	coupon = models.CharField(max_length=20, blank=False, null=False)
	discount = models.FloatField(default=0.1, blank=False, null=False)
	commission = models.FloatField(default=0.1, blank=False, null=False)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class InfluencerEarning(models.Model):
	influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
	total_amount = models.FloatField(default=0.0, blank=False, null=False)
	total_prices = models.FloatField(default=0.0, blank=False, null=False)
	total_shippings = models.FloatField(default=0.0, blank=False, null=False)
	total_sales = models.FloatField(default=0.0, blank=False, null=False)
	commission_earned = models.FloatField(default=0.0, blank=False, null=False)
	commission_paid = models.FloatField(default=0.0, blank=False, null=False)
	commission_owned = models.FloatField(default=0.0, blank=False, null=False)

	def pay(self):
		return mark_safe('<form action="/influencer/pay/" method="POST"><input style="display:none" name="influencer" value="'+str(self.influencer.id)+'"><input type="submit" value="Pay" formaction="/influencer/pay/"></form>')


class AllInfluencerSale(models.Model):
	influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	buyer = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='bought_by')
	seller = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='sold_by')
	commission = models.FloatField(default=0.1, blank=False, null=False)


class InfluencerPayHistory(models.Model):
	influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=datetime.now)
	amount = models.IntegerField(null=False, blank=False)