# Standard library imports
from django.shortcuts import render, redirect
from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Used to convert html to string during email
from django.template import loader
from urllib.parse import unquote
from datetime import datetime
import os
import random
import base64
import string
import json
import logging
import DNS

# Related third party imports
from Crypto.Cipher import AES

# Local application/library specific imports
from . import email_template
from . import constants as const
from . import models
from content.models import Content
from accounts.models import UserInfo
from accounts.utils import random_string, encrypt, decrypt
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email

def forgot_password_page(request):
	if request.user.is_authenticated:
		return redirect('index')
	""" This method is used to render the forgot password page.

	Args:
		request: The request object.

	Returns:
		It renders the forgot.html page.

	"""
	context = {'show':False}
	return render(request, 'pages/forgot.html', context)
	


def submit_email(request):
	""" This method is used to render the forgot password page with context.

	Args:
		request: The request object.

	Returns:
		It renders the forgot.html page.

	"""
	if request.user.is_authenticated:
		return redirect('index')
	try:
		with transaction.atomic():
			
			if request.method == 'POST':

				email_address = request.POST['email']

				if not User.objects.filter(email=email_address).exists():
					context = {'show': True}
					return render(request, 'pages/forgot.html', context)


				user = User.objects.get(email=email_address)

				obj = UserInfo.objects.get(user=user)

				to_email = email_address
				subject='Resetting your password for Bidgala'

				# Get user_info id
				text = str(obj.id)
				confirmation_str = random_string()

				filter_previous_change_request = models.PasswordRest.objects.filter(user=user)
				filter_previous_change_request.delete()
				password_reset_table = models.PasswordRest(user=user, verification_str=confirmation_str)
				password_reset_table.save()
					
				encrypted_text = str(encrypt(const.SECRET_KEY, text + ':' + confirmation_str) ,'utf-8')
				message_ = create_message(to_email, subject, email_template.getEmailVerificationTemplate(encrypted_text))
				try:
					sendgrid_send_email(message_)
				except Exception as e:
					logging.getLogger("error_logger").error(str(e))

				context = {'show': True}
				
			
			else:
				context = {'show': False}

			
			
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {'show': False}
	
	return render(request, 'pages/forgot.html', context)



def set_password_page(request, key):
	if request.user.is_authenticated:
		return redirect('index')
	try:
		with transaction.atomic():
			if key[0] == '+':
				key = key[1:]
			deciper_text = str(decrypt(const.SECRET_KEY, unquote(key)), 'utf-8')
			data = deciper_text.split(':')

			if len(data) != 2:
				return render(request, 'pages/setpassword.html', {'text':'The token is invalid.'})

			user_info = UserInfo.objects.all().filter(id=data[0])

			if user_info.exists():
				user = user_info.first()
				current_time = datetime.now()
				password_reset_object = models.PasswordRest.objects.filter(user=user.user, active=True, verification_str=data[1]).order_by('-request_time')
				
				if not password_reset_object.exists():
					return render(request, 'pages/setpassword.html', {'text':'The token is invalid.'})

				registered_time = password_reset_object.first().request_time.replace(tzinfo=None)

				diff = current_time - registered_time

				if diff.seconds <= const.EXPIRE_VERIFICATION_LINK:
					return render(request, 'pages/setpassword.html', {'integrate' : key})

				else:
					password_reset_object.delete()
					return render(request, 'pages/setpassword.html', {'text':'Link expired already.'})

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		raise Exception("Unable to process the request")



def change_password(request):
	if request.user.is_authenticated:
		return redirect('index')
	try:
		if request.method == 'POST':
			with transaction.atomic():
				password = request.POST['password'].strip()
				re_password = request.POST['repassword'].strip()

				if(password != re_password):
					return render(request, 'pages/setpassword.html', {'text':'Password do not match. Please try again.'})

				key = request.POST['key']
				deciper_text = str(decrypt(const.SECRET_KEY, unquote(key)), 'utf-8')
				data = deciper_text.split(':')

				if len(data) != 2:
					return render(request, 'pages/setpassword.html', {'text':'The token is invalid.'})

				user_info = UserInfo.objects.all().filter(id=data[0])

				if user_info.exists():
					user = user_info.first().user
					password_reset_object = models.PasswordRest.objects.filter(user=user, active=True, verification_str=data[1]).order_by('-request_time')
					user.set_password(password)

					password_reset_object.delete()
					user.save()

					return render(request, 'pages/setpassword.html', {'text':'Password changed. Please login using new credentials.'})

		

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, 'pages/setpassword.html', {'text':'Unable to change the password. Please try again.'})



