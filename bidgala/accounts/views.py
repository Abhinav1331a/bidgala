# Standard library imports
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import transaction
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import loader
from allauth.socialaccount.signals import pre_social_login
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import SuspiciousOperation
from allauth.exceptions import ImmediateHttpResponse
from django.conf import settings
from django.urls import reverse
import uuid
import logging
import base64
import json
import os
from datetime import datetime
import random
from urllib.parse import unquote
import string
import re
import DNS
import requests as external_requests
import sys
import requests

# Related third party imports
import stripe
from Crypto.Cipher import AES


# Local application/library specific imports
from exceptions.customs import *
from validate_email import validate_email
from . import constants as const
from . import email_template
from .utils import random_string, encrypt, decrypt, clear_messages
from payments.models import Stripe
from products.models import Product
from .models import UserInfo, TermsAndConditions
from .models import *
from . import choices
from products import choices as product_choices
from . import email_marketing
from .email import create_message, create_attachment, read_image, sendgrid_send_email
from influencer.models import Influencer


def account_verification(request, key):
	""" This method is called when user clicks verify button in verification email to verify their account

	Args:
		key: Encrypted field in email URL

	Returns:
		Sends a thank you email and redirects to email_verification.html page

	Raises:
		Token is invalid
		Account is already verified

	"""
	try:
		with transaction.atomic():
			if key[0] == '+':
				key = key[1:]
			deciper_text = str(decrypt(const.SECRET_KEY, unquote(key)), 'utf-8')
			data = deciper_text.split(':')

			if len(data) != 2:
				return render(request, 'pages/email_verification.html', {'text':'The token is invalid.'})

			user_info = UserInfo.objects.filter(id=data[0])

			if user_info.exists():
				user = user_info.first()
				current_time = datetime.now()

				registered_time = user.verification_expiry.replace(tzinfo=None)

				diff = current_time - registered_time

				if diff.seconds <= const.EXPIRE_VERIFICATION_LINK:

					if not user.verified:
						user.verified = True
						# request.session['user_verified'] = True

						# TODO code for referral
						if user.referred_by:
							referred_by_user = UserInfo.objects.filter(user=user.referred_by)[0]
							referred_by_user.num_of_referrals = referred_by_user.num_of_referrals + 1
							referred_by_user.bidgala_credits = referred_by_user.bidgala_credits + const.REFERRAL_CREDIT
							referred_by_user.save()
							
							user.bidgala_credits = user.bidgala_credits + const.REFERRAL_CREDIT


							customer_name = user.user.first_name + ' ' + user.user.last_name
							from_name = referred_by_user.user.first_name + ' ' + referred_by_user.user.last_name
							from_user_email = referred_by_user.user.email
							to_email = user.user.email
							subject = customer_name + ' ' + 'just joined Bidgala'

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

							message_ = create_message(from_user_email, subject, email_template.referralConfirmed(customer_name, from_name))

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

						user.save()

						customer_name = user.user.first_name + ' ' + user.user.last_name
						to_email = user.user.email
						subject = 'Welcome to Bidgala'

						#Here is the welcome email part.
						IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
						data1 = read_image(IMG_1_PATH)

						IMG_2_PATH = settings.BASE_DIR + '/bidgala/static/img/email/top.jpg'
						data2 = read_image(IMG_2_PATH)
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

						message_ = create_message(to_email, subject, email_template.getWelcomeTemplate(customer_name))


						attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
						attachment2 = create_attachment(data2, 'img/jpg', 'img2.jpg', 'img1')
						attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
						attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
						attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
						attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
						attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')

						message_.add_attachment(attachment1)
						message_.add_attachment(attachment2)
						message_.add_attachment(attachment_facebook)
						message_.add_attachment(attachment_twitter)
						message_.add_attachment(attachment_instagram)
						message_.add_attachment(attachment_linkedin)
						message_.add_attachment(attachment_pinterest)

						try:	
							sendgrid_send_email(message_)
						except Exception as e:
							logging.getLogger("error_logger").error(str(e))






						return render(request, 'pages/email_verification.html', {'text':'The email address verification is successful.'})
					else:
						return render(request, 'pages/email_verification.html', {'text':'The email address is already verified.'})

				else:
					return render(request, 'pages/email_verification.html', {'text':'This link is expired. Please try again.'})
			else:
				return render(request, 'pages/email_verification.html', {'text':'The token is invalid.'})

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		raise Exception("Unable to process the request")



@receiver(pre_social_login)
def handleDuplicateEmail(sender, request, sociallogin, **kwargs):


	if sociallogin.account.provider == 'google' or sociallogin.account.provider == 'facebook':
		email_address = sociallogin.account.extra_data['email']
		users = User.objects.all().filter(email=email_address)
		if users.exists():
			user = users.first()
			# if not user.userprofile.provider == sociallogin.account.provider:

			if (not SocialAccount.objects.all().filter(user_id = user.id).exists()) or (not SocialAccount.objects.get(user_id = user.id).provider == sociallogin.account.provider):

				raise ImmediateHttpResponse(redirect("index"))




@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
	""" This method is used to save the new user to UserInfo table.

	Args:
		sender: User object
		instance: To access the newly created user ojected
		created: To check whether an instance is created or not

	Raises:
		If exception raised the user record will be deleted

	"""
	try:

		if created:
			with transaction.atomic():

				referral_code = uuid.uuid5(uuid.NAMESPACE_DNS, str(instance.email)).hex[:8]
				email_without_domin = str(instance.email).split('@')[0] + str(instance.id)
				instance.username = email_without_domin
				instance.save()
				obj = UserInfo(user=instance, referral_code=referral_code.strip())
				obj.save()

				try:
					marketing_base_url = settings.MARKETING_TOOL_ADDRESS
					marketing_cipher = settings.MARKETING_TOOL_CIPHER
					marketing_encrypted_text = str(encrypt(marketing_cipher, instance.email) ,'utf-8')
					external_requests.get(marketing_base_url + marketing_encrypted_text)
				except Exception as e:
					logging.getLogger("error_logger").error('Error on line {}'.format(sys.exc_info()[-1].tb_lineno) + " : " + str(e))

				if settings.SERVER_TYPE_PRODUCTION:
					try:
						email_marketing.registerMailChimp(instance.email, instance.first_name, instance.last_name)
					except Exception as e:
						logging.getLogger("error_logger").error(str(e))
						

				# sending signup email to the user
				to_email = instance.email
				subject='Confirmation instructions'

				# Get user_info id
				text = str(obj.id)
				confirmation_str = random_string()

				obj.verification_str = confirmation_str

				obj.save()

				encrypted_text = str(encrypt(const.SECRET_KEY, text + ':' + confirmation_str) ,'utf-8')

				IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
				data1 = read_image(IMG_1_PATH)
				IMG_2_PATH = settings.BASE_DIR + '/bidgala/static/img/email/top.jpg'
				data2 = read_image(IMG_2_PATH)
				IMG_3_PATH = settings.BASE_DIR + '/bidgala/static/img/email/bottom.jpg'
				data3 = read_image(IMG_3_PATH)
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

				message_ = create_message(to_email, subject,email_template.getEmailVerificationTemplate(encrypted_text))
				attachment1 = create_attachment(data1, 'img/jpg', 'logo.jpg', 'logo')
				attachment2 = create_attachment(data2, 'img/jpg', 'top.jpg', 'img1')
				attachment3 = create_attachment(data3, 'img/jpg', 'bottom.jpg', 'img2')
				attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
				attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
				attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
				attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
				attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')
				message_.add_attachment(attachment1)
				message_.add_attachment(attachment2)
				message_.add_attachment(attachment3)
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
		# In case of any exception, delete the user record
		obj = User.objects.filter(id=instance.id)[0]
		obj.delete()
		logging.getLogger("error_logger").error(str(e))
		raise Exception("Unable to process the request")


@login_required
def verification_link_generator(request):
	user = UserInfo.objects.filter(user=request.user)[0]
	if not user.verified:
		registered_time = user.verification_expiry.replace(tzinfo=None)
		current_time = datetime.now()
		diff = current_time - registered_time

		to_email = user.user.email
		subject='Confirmation instructions'

		if diff.seconds > const.EXPIRE_VERIFICATION_LINK:
			text = str(obj.id)
			confirmation_str = random_string()
			user.verification_str = confirmation_str
			user.save()

		else:
			confirmation_str = user.verification_str

		
		text = str(user.id)
		encrypted_text = str(encrypt(const.SECRET_KEY, text + ':' + confirmation_str) ,'utf-8')
		IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
		data1 = read_image(IMG_1_PATH)
		IMG_2_PATH = settings.BASE_DIR + '/bidgala/static/img/email/top.jpg'
		data2 = read_image(IMG_2_PATH)
		IMG_3_PATH = settings.BASE_DIR + '/bidgala/static/img/email/bottom.jpg'
		data3 = read_image(IMG_3_PATH)
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

		message_ = create_message(to_email, subject,email_template.getEmailVerificationTemplate(encrypted_text))
		attachment1 = create_attachment(data1, 'img/jpg', 'logo.jpg', 'logo')
		attachment2 = create_attachment(data2, 'img/jpg', 'top.jpg', 'img1')
		attachment3 = create_attachment(data3, 'img/jpg', 'bottom.jpg', 'img2')
		attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
		attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
		attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
		attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
		attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')
		message_.add_attachment(attachment1)
		message_.add_attachment(attachment2)
		message_.add_attachment(attachment3)
		message_.add_attachment(attachment_facebook)
		message_.add_attachment(attachment_twitter)
		message_.add_attachment(attachment_instagram)
		message_.add_attachment(attachment_linkedin)
		message_.add_attachment(attachment_pinterest)

		if settings.SERVER_TYPE_PRODUCTION:
			try:
				sendgrid_send_email(message_)
			except Exception as e:
				logging.getLogger("error_logger").error(str(e))
		else:
			print('http://localhost:8001/confirmation/' + encrypted_text)
	return redirect('profile')


@login_required
def track_location(request):
	""" This method is used to track the user location
	"""

	try:

		loc = requests.get('https://ipapi.co/' + str(request.META['REMOTE_ADDR']) + '/json/')
		country_name = str(loc.json()['country_name'])
		city_name = str(loc.json()['city'])

		location_obj = Location.objects.filter(user=request.user)

		if location_obj.count() == 0:
			location_obj = Location(user=request.user, country=country_name, city=city_name)
			location_obj.save()
		else:
			location_obj = location_obj[0]
			country_ = location_obj.country.strip().split(' ')
			city_ = location_obj.city.strip().split(' ')

			if len(country_) == 3:
				country_.pop(0)
				city_.pop(0)

			country_.append(country_name)
			city_.append(city_name)

			countries = ' '.join(country_)
			ciites = ' '.join(city_)

			location_obj.country = countries
			location_obj.city = ciites

			location_obj.save()

		

		response = {
					'status' : 'success',
				}

		status_code = 200

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))

		response = {
					'status' : 'fail',
				}

		status_code = 500

	request.session['stop_track_location'] = True
	return JsonResponse(response, status=status_code)


@login_required
def set_account_type(request):
	""" This method is called to assign the account type to the user
	Account types may include seller, buyer or both.

	Args:
		request: The request object.

	Returns:
		It returns a JSONResponse

	"""

	try :
		if request.method == 'POST':

			val = request.POST['account_type'].strip()
			# region = request.POST['region'].strip()

			connect = ''
			if request.POST.get('connect'):
				connect = request.POST['connect'].strip()
			# country = request.POST['country'].strip()


			if (val not in ['b', 's', 'both', 'pro']):
				raise PostDataMissingException('Invalid data.')

			profession = ''

			if request.POST.get('cprofession'):
				if(request.POST['cprofession'] in choices.professions.keys()):
					profession = request.POST['cprofession'].strip()

			user_info = UserInfo.objects.get(user = request.user)

			if val == 'b':
				user_info.is_buyer = True
				user_info.is_seller = False
				user_info.is_professional = False
			elif val == 's':
				user_info.is_seller = True
				user_info.is_buyer = False
				user_info.is_professional = False
			elif val == 'both':
				user_info.is_seller = True
				user_info.is_buyer = True
				user_info.is_professional = False
			else:
				user_info.is_buyer = False
				user_info.is_seller = False
				user_info.is_professional = True

				if not (request.POST.get('cname')) and not (request.POST.get('cemail')) and not (request.POST.get('phone')):
					return redirect('index')

				user_info.company_name = request.POST['cname'].strip()
				user_info.company_email = request.POST['cemail'].strip()
				user_info.phone = request.POST['phone'].strip()
				user_info.company_website = request.POST['cweb'].strip()
				user_info.profession = profession

			# user_info.state = region
			user_info.connected_us = connect

			if request.POST.get('phone', None):
				user_info.phone = request.POST['phone'].strip()
			# user_info.country = country


			# if request.POST.get('agree', 'disagree') == 'agreed':
			# 	user_info.toc_agree = True
			# 	user_info.toc_agree_id = int(TermsAndConditions.objects.all().order_by('-date')[0].id)
			# else:
			# 	return redirect('index')

			user_info.save()

			if val == 'pro':
				# Send an email
				customer_name = request.user.first_name + ' ' + request.user.last_name

				to_email = request.POST['cemail'].strip()
				subject = 'Welcome to Bidgala'

				IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'

				data1 = read_image(IMG_1_PATH)

				message_ = create_message(to_email, subject, email_template.getWelcomeProfessionalTemplate(customer_name))

				attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
				message_.add_attachment(attachment1)

				try:
					sendgrid_send_email(message_)
				except Exception as e:
					logging.getLogger("error_logger").error(str(e))

			if settings.SERVER_TYPE_PRODUCTION:
				email_marketing.updateTagMailChimp(request.user.email, choices.TAGS[val])

			request.session['show_survey'] = False

		else:
			raise NotPostRequestException('Invalid request type.')


	except NotPostRequestException as e:
		logging.getLogger("error_logger").error(str(e))


	except PostDataMissingException as e:
		logging.getLogger("error_logger").error(str(e))


	except Exception as e:
		logging.getLogger("error_logger").error(str(e))


	return redirect('index_demo')



def add_referral(request):
	""" This method is called by an redirect call after new user is created.
	It is used to add the referred-by user name to the UserInfo table.

	Args:
		request: The request object.

	Returns:
		It renders the index_demo.html page.
	"""
	
	if request.user.is_authenticated:
		try:
			
			user = UserInfo.objects.get(user = request.user)
			request.session['user_verified'] = user.verified
			request.session['first_buy'] = user.first_buy


			if not request.session.get('referral_code'):
				request.session['referral_code'] = user.referral_code

			request.session['show_survey'] = False

			# track location
			request.session['track_location'] = True
			
			if (user.is_buyer == False) and (user.is_seller == False):
				if(user.is_professional == False):
					request.session['show_survey'] = True

			if user.profile_img:
				request.session['profile_img'] = user.profile_img.url


			referred_by_obj = None 
			if request.session.get("referred_by") :
				referred_by_obj = UserInfo.objects.get(referral_code__exact = request.session.get("referred_by").strip())
				user.referred_by = referred_by_obj.user
				user.save()					

		except Exception as e:
			logging.getLogger("error_logger").error(str(e))
			user.delete()
			del request.session['referred_by']

		clear_messages(messages, request)
		if request.session['show_survey']:
			#return redirect('index_demo')
			return render(request, 'pages/sign_up_transition.html')
 
	return redirect('index')




def referral_page(request):
	""" This method is used to render the referral page.

	Args:
		request: The request object.

	Returns:
		It renders the referral.html page.

	"""
	context = {}
	coupon_code = Influencer.objects.first().coupon
	# print(coupon_code)
	if request.user.is_authenticated:
		user_info = UserInfo.objects.get(user = request.user)
		if request.method == 'POST':
			context = {}
			to_email = request.POST['email']
			subject= request.user.first_name+" "+ request.user.last_name +' Has Invited You To Join Bidgala’s Art--Loving Community'
			IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'

			name = ''
			if len(user_info.user.first_name):
				name = user_info.user.first_name
			else:
				name = user_info.user.last_name

			referral_user_link = settings.HOST_BASE_URL + 'signup/' + user_info.referral_code + '/' + name
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

			message_ = create_message(to_email, subject, email_template.receiveReferralTemplate(request.user.first_name+" "+request.user.last_name, referral_user_link))

			attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
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

		if not request.session.get('referral_code'):
			request.session['referral_code'] = user_info.referral_code
			return render(request, 'referral/referral.html')
		else:
			request.session['referral_code'] = user_info.referral_code

			context['number_of_referrals'] = user_info.num_of_referrals
			context['user_donated_credits'] = user_info.donated_bidgala_credits

			# Since users may already have referrals and we are adding the bidgala credits field now, we first check if they have already donated (which means they have used up all their initial credits) in which case we have started to save credits to the new field in UserInfo rather than using the @property method and the correct credits will be available via user_info.bidgala_credits
			if user_info.donated_bidgala_credits > 0:
				context['user_bidgala_credits'] = user_info.bidgala_credits
			else:
				context['user_bidgala_credits'] = user_info.get_bidgala_credits

	context['category'] = product_choices.category
	context['subcategory'] = product_choices.subcategory
	context['coupon_code'] = coupon_code
	return render(request, 'referral/referral.html', context)



def register_referral(request, referral, name=''):
	""" This method is used to render the signup page with referral code.

	Args:
		request: The request object.

	Returns:
		It renders the register.html page.

	"""

	if request.user.is_authenticated:
		return redirect('index')

	if request.session.get('referred_by'):
		del request.session['referred_by']

	context = {}
	coupon_code = Influencer.objects.first().coupon
	if UserInfo.objects.filter(referral_code = referral.strip()).exists():

		context = {
		'has_referral' : True,
		'referral_code' : referral.strip(),
		'name' : name,
		'category':product_choices.category,
		'coupon_code' : coupon_code
		}

		request.session["referred_by"] = referral

	clear_messages(messages, request)
	return render(request, 'accounts/register.html', context)


def register(request):
	""" This method is used to render the signup page.

	Args:
		request: The request object.

	Returns:
		It renders the register.html page.

	"""

	# If user is already logged in, then redirect to index.html
	if request.user.is_authenticated:
		return redirect('index')

	# To clear the alert messages
	list(messages.get_messages(request))
	####

	request.messages = None
	return render(request, 'accounts/register.html', {'category':product_choices.category})



def create_user(request):
	""" This method is used to create new user.
	This method only takes POST request. Otherwise, it will redirect to
	register.html page with the error message.
	It also does baisc authentication including lenght of the password,
	email already exists etc.

	Minimum required password lenght is 8.

	Args:
		request: The request object.

	Returns:
		It redirects to the login page.

	"""

	# If user is already logged in, then redirect to index.html

	if request.user.is_authenticated:
		return redirect('index')

	request.messages = None
	request.session['show_survey'] = False
	try:

		if request.method == 'POST':
			any_error = False

			captcha_token = request.POST.get('g-recaptcha-response')
			cap_url = 'https://www.google.com/recaptcha/api/siteverify'
			cap_secret = settings.RECAPTCHA_PRIVATE_KEY
			cap_data = {
				'secret' : cap_secret,
				'response' : captcha_token
			}
			cap_server_response = requests.post(url=cap_url, data=cap_data)
			cap_json = json.loads(cap_server_response.text)
			if cap_json['success'] == False:
				messages.error(request, 'Invalid Captcha Try Again')
				return redirect('register')


			email = request.POST['email'].strip()
			password = request.POST['password'].strip()
			first_name = request.POST['first_name'].strip()
			last_name = request.POST['last_name'].strip()

			# Check if email already exists
			if User.objects.filter(email=email).exists():
				messages.error(request, 'Email already exists.')
				return redirect('register')

			if len(password) < 8:
				messages.error(request, 'Password is too short.')
				return redirect('register')

			# Check if email is valid using domain name

			is_valid = validate_email(email)
			if (is_valid is None) or (is_valid is False):
				messages.error(request, 'Invalid email address.')
				return redirect('register')

			if len(first_name) == 0:
				any_error = True
				messages.error(request, 'Please enter your first name.')

			is_valid = validate_email(email)
			if (is_valid is None) or (is_valid is False):
				messages.error(request, 'Invalid email address.')
				any_error = True


			if any_error:
				return render(request, 'accounts/register.html')

			user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
			user.save()
			user = auth.authenticate(email=email, password=password)

			if user is not None:
				auth.login(request, user)
				# Setting up session variables
				user_info = UserInfo.objects.get(user = user)
				request.session['is_seller'] = user_info.is_seller

				# If there is any reference, then we redirect referralcheck
				# to add the referred user

				if(request.session.get("referred_by")):					
					return redirect("referralcheck")


				user_info = UserInfo.objects.get(user = user)
				request.session['referral_code'] = user_info.referral_code

				if (user_info.is_buyer is False) and (user_info.is_seller is False):
						if(user_info.is_professional is False):
							request.session['show_survey'] = True

				#return redirect('index_demo')
				return render(request, 'pages/sign_up_transition.html')

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))

	messages.error(request, 'Something went wrong.')
	return redirect('register')


def login(request):
	""" This method is used to render the signin page.

	Args:
		request: The request object.

	Returns:
		It renders the register.html page.

	"""

	# If user is already logged in, then redirect to index.html
	if request.user.is_authenticated:
		return redirect('index')

	request.messages = None

	return render(request, 'accounts/login.html', {'category':product_choices.category})


def login_user(request):
	""" This method is used to authenticate user and login.
	This method only takes POST request. Otherwise, it will redirect to
	login.html page with the error message.
	The authentication including password and password verification.


	Minimum required password lenght is 8.

	Args:
		request: The request object.

	Returns:
		It redirects to the index page.

	"""

	# If user is already logged in, then redirect to index.html

	if request.user.is_authenticated:
		return redirect('index')

	try:
		request.messages = None
		if request.method == 'POST':

			email = request.POST['email'].strip()
			password = request.POST['password'].strip()

			if(request.session.get("referred_by")):
				del request.session["referred_by"]

			user = auth.authenticate(email=email, password=password)
			if user is not None:

				auth.login(request, user)

				# Setting up session variables
				user_info = UserInfo.objects.get(user = request.user)
				request.session['user_verified'] = user_info.verified
				if user_info.profile_img:
					request.session['profile_img'] = user_info.profile_img.url



				request.session['is_seller'] = user_info.is_seller
				request.session['referral_code'] = user_info.referral_code
				request.session['user_info_id'] = str(user_info.id)

				if (user_info.is_buyer is False) and (user_info.is_seller is False):
					if(user_info.is_professional is False):
						request.session['show_survey'] = True
				return redirect(request.META.get('HTTP_REFERER'))

	except Exception as e:
		# Need to add logs
		logging.getLogger("error_logger").error(str(e))


	messages.error(request, 'Something went wrong.')
	return redirect('login')




def logout(request):
	""" This method is used signout the user.
	This method only takes POST request. O

	Args:
		request: The request object.

	Returns:
		It redirects to the index page.

	"""

	# If user is not logged in, then redirect to index.html
	if not request.user.is_authenticated:
		return redirect('index')


	if request.method == 'POST':
		auth.logout(request)
	return redirect('index')

# Helper
def is_onboarding_complete(stripe_account):
	stripe.api_key = settings.STRIPE_SECRET_KEY

	seller_stripe_acc = stripe.Account.retrieve(stripe_account)

	if seller_stripe_acc.charges_enabled == False:
		onboarding_complete = False
		return seller_stripe_acc, onboarding_complete

	elif seller_stripe_acc.charges_enabled == True:
		onboarding_complete = True
		return seller_stripe_acc, onboarding_complete




def donate_credits(request):
	""" This method is used to allow users to submit their bidgala credits to admin

	Args:
		request: The request object.

	Returns:
		It redirects to the profile.html page.

	"""
	if request.user.is_authenticated and request.method == 'POST':
		try:
			donation_amount = int(request.POST['donation_amount'])


			if donation_amount:
				user_info = UserInfo.objects.get(user = request.user)
				user = User.objects.get(id=request.user.id)

				if user_info.donated_bidgala_credits > 0:
					CreditDonation.objects.create(user=user, donation_amount=donation_amount)
					user_info.donated_bidgala_credits = user_info.donated_bidgala_credits + donation_amount
					user_info.bidgala_credits = user_info.bidgala_credits - donation_amount
					user_info.save()

				else:
					CreditDonation.objects.create(user=user, donation_amount=donation_amount)
					user_info.donated_bidgala_credits = user_info.donated_bidgala_credits + donation_amount

					user_info.save()

			messages.success(request, 'Thank you for your donation!')
			response = {'status' : 'success'}

		except Exception as e:
			response = {'error' : 'error'}
			logging.getLogger("error_logger").error(str(e))

		return JsonResponse(response)
	else:
		request.messages = None
		messages.error(request, 'Please login to donate')
		return redirect('login')




def user_settings(request):
	""" This method is used to display the user settings page.
	This method only takes POST request. Otherwise, it will redirect to
	login.html page with the error message.


	Args:
		request: The request object.

	Returns:
		It redirects to the profile.html page.

	"""

	# If user is not logged in, then redirect to login.html
	coupon_code = Influencer.objects.first().coupon
	if request.user.is_authenticated:
		clear_messages(messages, request)
		context = {
			'account_type' : choices.account_type,
			'country' : choices.country,
		}

		user_info = UserInfo.objects.get(user = request.user)
		user = User.objects.get(id=request.user.id)

		if Stripe.objects.filter(user=user_info).count() == 1:
			user_stripe_acc = Stripe.objects.get(user=user_info)
			context['user_stripe_acc'] = user_stripe_acc
			seller_stripe_acc, onboarding_complete = is_onboarding_complete(user_stripe_acc.stripe_account_id)
			if onboarding_complete == True:
				context['onboarding_complete'] = True
				context['seller_stripe_acc'] = seller_stripe_acc
			else:
				context['onboarding_complete'] = False
				context['seller_stripe_acc'] = seller_stripe_acc
		else:
			context['user_stripe_account'] = None


		context['user_donated_credits'] = user_info.donated_bidgala_credits

		# Since users may already have referrals and we are adding the bidgala credits field now, we first check if they have already donated (which means they have used up all their initial credits) in which case we have started to save credits to the new field in UserInfo rather than using the @property method and the correct credits will be available via user_info.bidgala_credits
		if user_info.donated_bidgala_credits > 0:
			context['user_bidgala_credits'] = user_info.bidgala_credits
		else:
			context['user_bidgala_credits'] = user_info.get_bidgala_credits


		context['blog'] = user_info.get_blog
		context['newsletter'] = user_info.get_newsletter
		context['offer'] = user_info.get_personal_offer
		context['account_verified'] = user_info.verified

		request.session['user_verified'] = user_info.verified

		if user_info.id:
			context['user_info_id'] = user_info.id

		if user_info.profile_img:
			context['profile_img'] = user_info.profile_img.url

		if len(request.user.username.strip()) > 0:
			context['username'] = request.user.username.strip()

		if len(user_info.country.strip()) > 0 and len(user_info.state.strip()):
			country = user_info.country
			region = user_info.state.strip()

			try:
				context['location'] = choices.country[country]['states'][region]
			except Exception as e:
				context['location'] = ''



		if len(user_info.phone.strip()) > 0:
			context['phone'] = user_info.phone

		if len(user_info.bio.strip()) > 0:
			context['bio'] = user_info.bio

		if len(user_info.instagram_username.strip()) >0:
			context['instagram'] = user_info.instagram_username

		if len(user_info.twitter_username.strip()) >0:
			context['twitter'] = user_info.twitter_username

		if len(user_info.linkedin_link.strip()) >0:
			context['linkedin'] = user_info.linkedin_link

		if len(user_info.facebook_link.strip()) >0:
			context['facebook'] = user_info.facebook_link

		if len(user.email.strip()) > 0:
			context['email'] = user.email

		if len(user.first_name.strip()) > 0:
			context['firstname'] = user.first_name


		if len(user.last_name.strip()) > 0:
			context['lastname'] = user.last_name


		if len(user_info.headline.strip()) > 0:
			context['headline'] = user_info.headline


		if user_info.is_buyer and not user_info.is_seller:
			context['account'] = 'Buyer'
			context['account_value'] = 'b'

		elif user_info.is_seller and not user_info.is_buyer:
			context['account'] = 'Seller'
			context['account_value'] = 's'

		elif user_info.is_professional:
			context['account'] = 'Professional'
			context['account_value'] = 'pro'
			context['cname'] = user_info.company_name
			context['cemail'] = user_info.company_email
			context['cverify'] = user_info.company_email_verified
			context['cweb'] = user_info.company_website

		else:
			context['account'] = 'Buyer & Seller'
			context['account_value'] = 'both'

		context['joined'] = user.date_joined.strftime("%d %b %Y")
		context['last_login'] = user.last_login
		context['category'] = product_choices.category
		context['coupon_code'] = coupon_code

		return render(request, 'profile/user_settings.html', context)

	
	messages.error(request, 'Please login to access the profile page.')
	return redirect('login')



def profile_img_update(request):
	""" This method is used to update the profile picture.
	This method only takes POST request. Otherwise, it will redirect to
	login.html page with the error message.


	Args:
		request: The request object.

	Returns:
		It redirects to the profile.html page.

	"""
	if request.user.is_authenticated:
		if request.method == 'POST':
			try:
				img = request.FILES['user_profile_pic']
				if img:
					user_info = UserInfo.objects.get(user = request.user)

					# Remove old profile picture
					user_info.profile_img.delete()
					user_info.profile_img = img
					user_info.save()
					request.session['profile_img'] = user_info.profile_img.url
					messages.success(request, 'Profile picture updated.')

			except Exception as e:
				logging.getLogger("error_logger").error(str(e))
			return redirect('profile')


	request.messages = None
	messages.error(request, 'Please login to access the profile page.')
	return redirect('login')


def account_update(request):
	""" This method is used to update the user account information from the settings page.
	This method only takes POST request. Otherwise, it will redirect to
	login.html page with the error message.


	Args:
		request: The request object.

	Returns:
		It redirects to the user_settings.html page.

	"""

	# If user is not logged in, then redirect to login.html


	if request.user.is_authenticated:

		if request.method == 'POST':

			try:

				with transaction.atomic():
					user_info = UserInfo.objects.get(user = request.user)
					user = User.objects.get(id = request.user.id)

					# Updating profile data

					if len(request.POST['username'].strip()) == 0:
						raise UserNameEmptyException('Username is empty.')

					if len(request.POST['firstname'].strip()) == 0:
						raise InvalidFormatException('first name cannot be digits or empty.')


					if User.objects.filter(username=request.POST['username'].
						strip()).exclude(id=request.user.id).exists():
						raise UserNameExistsException('Username already exists.')

					if request.POST['phone'] and len(re.findall(r'\d{3}\d{3}\d{4}', request.POST['phone'])) == 0:
						raise InvalidFormatException('Invalid phone number.')


					if request.session.get("is_seller") :
						del request.session["is_seller"]


					user.username = request.POST['username'].strip()

					user_info.bio = request.POST['bio'].strip()

					user.first_name = request.POST['firstname'].strip()

					user.last_name = request.POST['lastname'].strip()

					user_info.headline = request.POST['headline'].strip()

					user_info.phone = request.POST['phone'].strip()

					user_info.instagram_username = request.POST['instagram'].strip()

					user_info.twitter_username = request.POST['twitter'].strip()

					user_info.facebook_link = request.POST['facebook'].strip()

					user_info.linkedin_link = request.POST['linkedin'].strip()


					if len(request.POST['lastname'].strip()) == 0:
						user.last_name = request.POST['lastname'].strip()

					if request.POST.get('country') and request.POST.get('country', '') in choices.country.keys():
						user_info.country = request.POST['country'].strip()




					if (request.POST.get('country', None)) and (request.POST.get('region', '') in list(choices.country[request.POST['country']]['states'].keys())):
						user_info.state = request.POST['region'].strip()



					# Check if account_type is valid input or not
					if not (request.POST.get('account_type') and request.POST.get('account_type') in ['b', 's', 'both', 'pro']):
						raise InvalidFormatException('Choose a valid account type')

					if request.POST['account_type'] == 'b':
						user_info.is_buyer = True
						user_info.is_seller = False
						user_info.is_professional = False


					elif request.POST['account_type'] == 's':
						user_info.is_buyer = False
						user_info.is_seller = True
						user_info.is_professional = False
						request.session['is_seller'] = True

					elif request.POST['account_type'] == 'pro':
						user_info.is_buyer = False
						user_info.is_seller = False
						user_info.is_professional = True

						if not request.POST.get('phone') or len(re.findall(r'\d{3}\d{3}\d{4}', request.POST['phone'])) == 0:
							raise InvalidFormatException('Invalid phone number.')

						if not request.POST.get('cname') or len(request.POST['cname'].strip()) == 0:
							raise InvalidFormatException('Please enter company name')

						if not request.POST.get('cemail') or len(request.POST['cemail'].strip()) == 0:
							raise InvalidFormatException('Please enter company email')


						if(user_info.company_name != request.POST['cname'].strip()) or (user_info.company_email != request.POST['cemail'].strip()):

							user_info.company_name = request.POST['cname'].strip()
							user_info.company_email = request.POST['cemail'].strip()
							user_info.company_email_verified = False

						if(user_info.company_website != request.POST['cweb'].strip()):
							user_info.company_website = request.POST['cweb'].strip()


					else:
						user_info.is_buyer = True
						user_info.is_seller = True
						user_info.is_professional = False
						request.session['is_seller'] = True


					if request.POST['blog'] == 'true':
						user_info.get_blog = True
					else:
						user_info.get_blog = False


					if request.POST['newsletter'] == 'true':
						user_info.get_newsletter = True
					else:
						user_info.get_newsletter = False

					if request.POST['offer'] == 'true':
						user_info.get_personal_offer = True
					else:
						user_info.get_personal_offer = False



					user_info.save()
					user.save()


			except UserNameExistsException as e:

				response = {
					'status' : 'fail',
					'message' : str(e),
				}

				return JsonResponse(response)

			except UserNameEmptyException as e:

				response = {
					'status' : 'fail',
					'message' : str(e),
				}

				return JsonResponse(response)

			except InvalidFormatException as e:


				response = {
					'status': 'fail',
					'message': str(e),
				}

				return JsonResponse(response)

			except Exception as e:

				response = {
					'status' : 'fail',
					'message' : 'Something went wrong',
				}

				logging.getLogger("error_logger").error(str(e))
				return JsonResponse(response)


			response = {
					'status' : 'success',
					'message' : 'Changes saved',
				}

			return JsonResponse(response)


	request.messages = None
	messages.error(request, 'Please login to access the profile page.')
	return redirect('login')



def art_upload_page(request):
	""" This method is redirect to the art upload page.

	Args:
		request: The request object.

	Returns:
		It renders the art_upload.html page.

	"""

	# If user is already logged in, then redirect to index.html
	if request.user.is_authenticated:

		show_page = False
		user = UserInfo.objects.get(user = request.user)

		if Stripe.objects.filter(user=user).count() == 1:
			show_page = True

		stripe_account = Stripe.objects.filter(user=user)
		onboarding_complete = False
		if stripe_account.count() > 0:
			stripe_account = stripe_account[0]
			onboarding_complete = is_onboarding_complete(stripe_account.stripe_account_id)

		content = {
			'category' : product_choices.category,
			'category_sell' : product_choices.category_sell,
			'dim_measurement' : product_choices.dim_measurement,
			'style' : product_choices.styles,
			'material' : product_choices.material,
			'show_page' : show_page,
			'onboarding_complete': onboarding_complete
		}

		return render(request, 'products/art_upload.html', content)

	request.messages = None
	messages.error(request, 'Please login to access the sell page.')
	return redirect('login')



def get_sub_categories(request):

	""" This method is send subcategory list for ajax request.

	Args:
		request: The request object.

	Returns:
		jsonObject.

	"""

	try :
		if request.method == 'POST':


			category_json = json.loads(request.body)
			category = category_json['category']

			response = {
						'status' : 'success',
						'data' : product_choices.subcategory[category]
					}
		else:
			raise NotPostRequestException('Invalid request type.')


	except NotPostRequestException as e:

		response = {
					'status' : 'fail',
					'message' : str(e),
				}

	except Exception as e:

		response = {
					'status' : 'fail',
					'message' : str(e),
				}


	return JsonResponse(response)


def public_profile(request, slug):

	""" This method renders the public profile page

	Args:
		request: The request object.

	Returns:
		Renders public profile page

	"""

	try:
		try:
			user = User.objects.get(username=slug)
			userInfo = UserInfo.objects.get(user=user)
		except User.DoesNotExist:
			userInfo = UserInfo.objects.get(id=slug)
			user = User.objects.get(id=userInfo.user.id)


		# get all followings that the request user has
		coupon_code = Influencer.objects.first().coupon
		if request.user.is_authenticated:
			if UserFollowing.objects.filter(user_id=request.user, following_user_id=user):
				request_user_follows = True
			else:
				request_user_follows = False
		else:
			request_user_follows = False



		try:
			user_followers = UserFollowing.objects.filter(following_user_id=user).count()
			user_followings = UserFollowing.objects.filter(user_id=user).count()
		except UserFollowing.DoesNotExist:
			user_followers = 0
			user_followings = 0


		try:
			headerImage = HeaderImage.objects.get(user=user)

		except HeaderImage.DoesNotExist:
			headerImage = None


		try:
			featuredWorks = FeaturedWork.objects.filter(user=user)
			featuredWorksCount = FeaturedWork.objects.filter(user=user).count()

		except FeaturedWork.DoesNotExist:
			featuredWorks = None
			featuredWorksCount = None

		try:
			artistStatement = ArtistStatement.objects.get(user=user)

		except ArtistStatement.DoesNotExist:
			artistStatement = None

		try:
			educations = Education.objects.filter(user=user).order_by('-start_year')

			if request.method == 'POST' and request.is_ajax() and request.POST.get('section') == 'education':
				ID = request.POST.get('id')
				education = educations.get(id=ID)
			else:
				education = None


		except Education.DoesNotExist:
			educations = None


		try:
			skills_obj = Skill.objects.get(user=user)
			if not skills_obj.skills:
				skills_obj.delete()
				skills = None
			else:
				skills_array = skills_obj.skills.split(",")
				skills_string = skills_obj.skills

		except Skill.DoesNotExist:
			skills = None
			skills_array = None
			skills_string = None

		try:
			interests_obj = Interest.objects.get(user=user)
			if not interests_obj.interests:
				interests_obj.delete()
				interests = None
			else:
				interests_array = interests_obj.interests.split(",")
				interests_string = interests_obj.interests

		except Interest.DoesNotExist:
			interests = None
			interests_array = None
			interests_string = None


		try:
			awards = Accomplishment.objects.filter(user=user, accomplishment_type="Award").order_by('-year', '-month')
			press = Accomplishment.objects.filter(user=user, accomplishment_type="Press").order_by('-year', '-month')
			projects = Accomplishment.objects.filter(user=user, accomplishment_type="Project").order_by('-year', '-month')


			if request.method == 'POST' and request.is_ajax() and request.POST.get('section') == 'accomplishment':
				ID = request.POST.get('id')
				accomplishment = Accomplishment.objects.get(id=ID)
			else:
				accomplishment = None

		except Accomplishment.DoesNotExist:
			awards = None
			press = None
			projects = None

		try:
			exhibitions = Exhibition.objects.filter(user=user).order_by('-year', '-month')

			if request.method == 'POST' and request.is_ajax() and request.POST.get('section') == 'exhibition':
				ID = request.POST.get('id')
				exhibition = Exhibition.objects.get(id=ID)
			else:
				exhibition = None

		except Exhibition.DoesNotExist:
			exhibitions = None


		try:
			products = Product.objects.filter(owner=userInfo, available=True).order_by('-date')

		except Product.DoesNotExist:
			products = None



		context = {
			"user_": user,
			"userInfo": userInfo,
			"artistStatement": artistStatement,
			"educations": educations,
			"years": choices.years,
			"skills": skills_array,
			"skills_string": skills_string,
			"interests": interests_array,
			"interests_string": interests_string,
			"months": choices.months,
			"awards": awards,
			"press": press,
			"projects": projects,
			"exhibitions": exhibitions,
			"country": choices.country,
			"products": products,
			"headerImage": headerImage,
			"featuredWorks": featuredWorks,
			"featuredWorksCount": featuredWorksCount,
			"education": education,
			"accomplishment": accomplishment,
			"exhibition": exhibition,
			"request_user_follows": request_user_follows,
			"user_followers": user_followers,
			"user_followings": user_followings,
			"BASE_URL": settings.HOST_BASE_URL,
			"BASE_S3_URL": settings.BASE_AWS_IMG_URL,
			'category' : product_choices.category,
			'coupon_code': coupon_code,
			'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
			}

 

		return render(request, "profile/public_profile.html", context)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_404.html")






#Artist Statement
def add_artist_statement(request):
	""" This method adds artist statement to the users public profile

	Args:

	Returns:
		Redirects back to the public profile

	Raises:


	"""
	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				current_user = User.objects.get(username=username)
				statement_text = request.POST['artist-statement']
				statement = ArtistStatement.objects.create(user = current_user, statement = statement_text)
				statement.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)



def edit_artist_statement(request):
	""" This method edits artist statement for the users public profile

	Args:

	Returns:
		Redirects back to the public profile

	Raises:


	"""



	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				statement_text = request.POST['artist-statement']
				current_user = User.objects.get(username=username)
				ArtistStatement.objects.filter(user = current_user).update(statement=statement_text)

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def delete_artist_statement(request):


	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				current_user = User.objects.get(username=username)
				ArtistStatement.objects.get(user = current_user).delete()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")


def add_education(request):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				school = request.POST['school']
				degree = request.POST['degree']
				field_of_study = request.POST['field-of-study']
				start_year = request.POST['start-year']
				end_year = request.POST['end-year']
				description = request.POST['des']
				current_user = User.objects.get(username=username)
				education = Education.objects.create(
					user = current_user,
					school = school,
					degree = degree,
					field_of_study = field_of_study,
					start_year = start_year,
					end_year = end_year,
					description = description
					)

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def edit_education(request, educationid):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				school = request.POST['school']
				degree = request.POST['degree']
				field_of_study = request.POST['field-of-study']
				start_year = request.POST['start-year']
				end_year = request.POST['end-year']
				description = request.POST['des']
				current_user = User.objects.get(username=username)
				education = Education.objects.get(user=current_user, id=educationid)
				education.user = current_user
				education.school = school
				education.degree = degree
				education.field_of_study = field_of_study
				education.start_year = start_year
				education.end_year = end_year
				education.description = description
				education.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)



def delete_education(request, educationid):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				current_user = User.objects.get(username=username)
				Education.objects.get(user=current_user, id=educationid).delete()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")


def add_skills(request):
	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				skills = request.POST['skills']
				current_user = User.objects.get(username=username)
				skills_obj = Skill.objects.create(
					user = current_user,
					skills = skills,
				)
				skills_obj.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def delete_skills(request):



	try:
		username = request.user.username
		current_user = User.objects.get(username=username)
		Skill.objects.get(user=current_user).delete()
		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")


def edit_skills(request):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				skills = request.POST['skills']
				current_user = User.objects.get(username=username)
				skills_obj = Skill.objects.get(user=current_user)
				skills_obj.skills = skills
				skills_obj.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def add_interests(request):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				interests = request.POST['interests']
				current_user = User.objects.get(username=username)
				interests = Interest.objects.create(
					user = current_user,
					interests = interests,
				)
				interests.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def delete_interests(request):
	try:
		username = request.user.username
		current_user = User.objects.get(username=username)
		Interest.objects.get(user=current_user).delete()
		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")


def edit_interests(request):
	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				interests = request.POST['interests']
				current_user = User.objects.get(username=username)
				interests_obj = Interest.objects.get(user=current_user)
				interests_obj.interests = interests
				interests_obj.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def add_accomplishment(request):
	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				accomplishment_type = request.POST['type']
				title = request.POST['title']
				description = request.POST['description']
				link = request.POST['link']
				month = request.POST['month']
				year = request.POST['year']
				current_user = User.objects.get(username=username)
				accomplishment = Accomplishment.objects.create(
					user = current_user,
					accomplishment_type = accomplishment_type,
					title = title,
					description = description,
					link = link,
					month = month,
					year = year
					)
				accomplishment.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)



def delete_accomplishment(request, accid):
	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				current_user = User.objects.get(username=username)
				Accomplishment.objects.get(user=current_user, id=accid).delete()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")


def edit_accomplishment(request, accid):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				accomplishment_type = request.POST['type']
				title = request.POST['title']
				description = request.POST['description']
				link = request.POST['link']
				month = request.POST['month']
				year = request.POST['year']
				current_user = User.objects.get(username=username)
				accomplishment = Accomplishment.objects.get(user=current_user, id=accid)
				accomplishment.user = current_user
				accomplishment.accomplishment_type = accomplishment_type
				accomplishment.title = title
				accomplishment.description = description
				accomplishment.link = link
				accomplishment.month = month
				accomplishment.year = year
				accomplishment.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def add_exhibition(request):

	try:
		username = request.user.username
		if request.user.is_authenticated:
			if request.method == 'POST':
				title = request.POST['title']
				location = request.POST['location']
				description = request.POST['description']
				link = request.POST['link']
				month = request.POST['month']
				year = request.POST['year']
				current_user = User.objects.get(username=username)
				exhibitions = Exhibition.objects.create(
					user = current_user,
					location = location,
					title = title,
					description = description,
					link = link,
					month = month,
					year = year
					)
				exhibitions.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_404.html")


def delete_exhibition(request, exid):


	try:

		if request.user.is_authenticated:
			username = request.user.username
			if request.method == 'POST':
				current_user = User.objects.get(username=username)
				Exhibition.objects.get(user=current_user, id=exid).delete()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")


def edit_exhibition(request, exid):

	try:

		if request.user.is_authenticated:
			username = request.user.username
			if request.method == 'POST':
				title = request.POST['title']
				location = request.POST['location']
				description = request.POST['description']
				link = request.POST['link']
				month = request.POST['month']
				year = request.POST['year']
				current_user = User.objects.get(username=username)
				exhibition = Exhibition.objects.get(user=current_user, id=exid)
				exhibition.user = current_user
				exhibition.title = title
				exhibition.location = location
				exhibition.description = description
				exhibition.link = link
				exhibition.month = month
				exhibition.year = year
				exhibition.save()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)


def edit_header_image(request):
	""" This method is used to update the header image.
	This method only takes POST request.


	Args:
		request: The request object.

	Returns:
		It redirects to the public_profile.html page.

	"""

	if request.user.is_authenticated:
		username = request.user.username
		if request.method == 'POST':
			header_img = request.FILES['user_header_img']
			if header_img:
				try:
					header_img_obj = HeaderImage.objects.get(user = request.user)

					if header_img_obj:
						# Remove old header picture
						header_img_obj.header_image.delete()

						header_img_obj.header_image = header_img
						header_img_obj.save()

						request.session['header_img'] = header_img_obj.header_image.url

						messages.success(request, 'Header image updated.')

				except HeaderImage.DoesNotExist:
					HeaderImage.objects.create(user = request.user, header_image=header_img)

				return redirect("public_profile", username)

	request.messages = None
	messages.error(request, 'Please login to access the profile page.')
	return redirect('login')



def add_featured_work(request):
	""" This method is used to upload a featured image.
	This method only takes POST request.


	Args:
		request: The request object.

	Returns:
		It redirects to the public_profile.html page.

	"""

	try:
		if request.user.is_authenticated:
			username = request.user.username
			if request.method == 'POST':
				featured_img = request.FILES['featured_work_image']
				title = request.POST['featured_work_title']
				description = request.POST['featured_work_description']

				featured_work_obj = FeaturedWork.objects.filter(user = request.user)
				user_total_featured_works = featured_work_obj.count()

				if user_total_featured_works != 6:
					FeaturedWork.objects.create(user=request.user, title=title, description=description, art_image=featured_img)

		return redirect("public_profile", username)


	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Something went wrong: Check character length or try again later')
		return redirect("public_profile", username)



def delete_featured_work(request, artid):
	username = request.user.username

	try:
		if request.user.is_authenticated:
			if request.method == 'POST':
				FeaturedWork.objects.get(user=request.user, id=artid).delete()

		return redirect("public_profile", username)

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		return render(request, "error/error_500.html")



def follow_user(request):
	try:
		if request.user.is_authenticated:

			if request.method == 'POST' and request.is_ajax():

				user_to_follow_id = request.POST['user_id']
				user_to_follow = User.objects.get(id=user_to_follow_id)

				UserFollowing.objects.create(user_id=request.user, following_user_id=user_to_follow)

				try:
					if request.user != user_to_follow:
							from_email = settings.FROM_EMAIL
							to_email = user_to_follow.email

							subject='You have a new follower'



							following_person_name = request.user.first_name + ' ' + request.user.last_name
							link_to_profile = settings.HOST_BASE_URL + 'p/' + request.user.username

							# TODO : PUT EMAIL CODE HERE
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
							message_ = create_message(to_email, subject, email_template.followingEmail(link_to_profile, following_person_name))

							attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
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

				response = {'status' : 'success'}

			else:
				response = {'status' : 'Not a post call'}
		else:
			response = {'status' : 'User not authenticated'}

	except Exception as e:
		response = {'status' : 'Error'}

	return JsonResponse(response)


def unfollow_user(request):
	try:
		if request.user.is_authenticated:
			if request.method == 'POST' and request.is_ajax():

				user_to_unfollow_id = request.POST['user_id']
				user_to_unfollow = User.objects.get(id=user_to_unfollow_id)

				UserFollowing.objects.get(user_id=request.user, following_user_id=user_to_unfollow).delete()

				response = {'status' : 'success'}

			else:
				response = {'status' : 'Not a post call'}

		else:
			response = {'status' : 'User not authenticated'}

	except Exception as e:
		response = {'status' : 'Error'}

	return JsonResponse(response)
