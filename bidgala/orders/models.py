from django.db import models
from datetime import datetime


from accounts.models import UserInfo
import products

# Create your models here.

class Inquiry(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(products.models.Product, on_delete=models.CASCADE, null=True)
    payment_type = models.CharField(max_length=20, blank=True)   
    first_name = models.CharField(max_length=50, blank=True)   
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    apt_number = models.CharField(max_length=40, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    accepted = models.BooleanField(blank=False, default=False)
    created_date = models.DateTimeField(default=datetime.now)
    
