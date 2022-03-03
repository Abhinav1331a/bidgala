from django.db import models
from datetime import datetime
from accounts.models import UserInfo

# Create your models here.

class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added =  models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.email