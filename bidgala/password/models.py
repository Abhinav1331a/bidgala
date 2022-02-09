from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import uuid
import base64

class PasswordRest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	active = models.BooleanField(default=True, blank=False)
	verification_str = models.TextField(blank=False)
	request_time = models.DateTimeField(default=datetime.now, blank=False)

	def __str__(self):
		return self.user.email