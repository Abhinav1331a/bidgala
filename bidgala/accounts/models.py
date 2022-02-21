# Standard library imports
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.html import mark_safe
from django.conf import settings
from datetime import datetime
import uuid
import base64

# Related third party imports
import stripe
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)

# Local application/library specific imports
from . import email_template
from . import constants as const
# from payments.models import Stripe
import payments

def path_edit(instance, filename):
	return '/'.join(['userinfo', str(instance.id), 'profile_img', filename])

def path_edit_header_img(instance, filename):
	return '/'.join(['header', str(instance.id), 'header_img' +  filename])

def path_edit_featured_work(instance, filename):
	return '/'.join(['featuredwork', str(instance.id), 'featured_work_img' +  filename])

def path_edit_category_img(instance, filename):
	return '/'.join(['category_display', str(instance.id) + '_' +  filename])

class UserInfo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
	verified = models.BooleanField(default=False, blank=False)
	featured_artist = models.BooleanField(default=False, blank=False)
	verification_str = models.TextField(blank=True)
	verification_expiry = models.DateTimeField(default=datetime.now, blank=True)
	profile_img = models.ImageField(upload_to=path_edit, blank=True)
	country = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=20, blank=True)
	state = models.CharField(max_length=20, blank=True)
	zip_code = models.CharField(max_length=20, blank=True)
	bio = models.CharField(max_length=1500, blank=True)
	phone = models.CharField(max_length=15, blank=True)
	is_buyer = models.BooleanField(default=False)
	is_seller = models.BooleanField(default=False)
	is_professional = models.BooleanField(default=False)
	profession = models.CharField(max_length=50, blank=True)
	referred_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, default=None)
	first_buy = models.BooleanField(default=False)
	first_sell = models.BooleanField(default=False)
	referral_code = models.TextField(blank=True)
	referral_bonus = models.IntegerField(default=0, blank=False)
	any_discount = models.BooleanField(default=False)
	discount_percent = models.IntegerField(default=0, blank=False)
	num_of_referrals = models.IntegerField(default=0, blank=False)
	connected_us = models.CharField(max_length=10, blank=True) 
	cash_earned = models.IntegerField(default=0, blank=False)
	artist_is = models.CharField(max_length=500, blank=True) 
	get_blog = models.BooleanField(default=True)
	get_newsletter = models.BooleanField(default=True)
	get_personal_offer = models.BooleanField(default=True)
	company_name = models.CharField(max_length=150, blank=True)
	company_email = models.CharField(max_length=150, blank=True)
	company_website = models.CharField(max_length=150, blank=True)
	company_email_verified = models.BooleanField(default=False)
	instagram_username = models.CharField(max_length=150, blank=True)
	twitter_username = models.CharField(max_length=150, blank=True)
	facebook_link = models.CharField(max_length=200, blank=True)
	linkedin_link = models.CharField(max_length=200, blank=True)
	headline = models.CharField(max_length=70, blank=True)
	bidgala_credits = models.IntegerField(default=0, blank=False)
	donated_bidgala_credits = models.IntegerField(default=0, blank=False)
	stripe_customer_id = models.CharField(max_length=200, blank=True)
	toc_agree = models.BooleanField(default=False)
	toc_agree_id = models.IntegerField(null=True, blank=True)
	special_user = models.BooleanField(default=False)

	def stripe_onboarding_status_info(self, stripe_account):
		stripe.api_key = settings.STRIPE_SECRET_KEY

		seller_stripe_acc = stripe.Account.retrieve(stripe_account)

		if seller_stripe_acc.charges_enabled == False:
			onboarding_complete = False
			return seller_stripe_acc, onboarding_complete

		elif seller_stripe_acc.charges_enabled == True:
			onboarding_complete = True
			return seller_stripe_acc, onboarding_complete


	# This is useful for sending confirmation emails to professionals upon confirmation
	# from admin page
	def save(self, *args, **kwargs):
		if self.id:
			cls = self.__class__
			old = cls.objects.filter(id=self.id)
			if old.count() > 0:
				old = old[0]
				new = self
				changed_fields = []
				for field in cls._meta.get_fields():
					 field_name = field.name
					 try:
					 	if getattr(old, field_name) != getattr(new, field_name):
					 		changed_fields.append(field_name)
					 except Exception as ex:
					 	pass


				if 'company_email_verified' in changed_fields:
					kwargs['update_fields'] = changed_fields
					if (old.company_email_verified != new.company_email_verified) and (new.company_email_verified):
						customer_name = old.user.first_name + ' ' + old.user.last_name

						from_email = settings.FROM_EMAIL
						to_email = old.company_email
						subject='Notification on your Professional Account'

						IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
						with open(IMG_1_PATH, 'rb') as f:
							data1 = f.read()
							f.close()

						message = Mail(
								from_email=from_email,
				    		 	to_emails=to_email,
				   				subject=subject,
				 		    	html_content=email_template.getProfessionalConfirmTemplate(customer_name)
				 		    )

						encoded1 = base64.b64encode(data1).decode()
						attachment1 = Attachment()
						attachment1.file_content = FileContent(encoded1)
						attachment1.file_type = FileType('img/png')
						attachment1.file_name = FileName('logo.png')
						attachment1.disposition = Disposition('inline')
						attachment1.content_id = ContentId('logo')
						message.add_attachment(attachment1)
						sendgrid_api_key = settings.SENDGRID_API_KEY
						sg = SendGridAPIClient(sendgrid_api_key)
						try:
							response = sg.send(message)	
						except Exception as e:
							logging.getLogger("error_logger").error(str(e))
		
		super().save(*args, **kwargs)

	@property
	def get_bidgala_credits(self):
		if self.referred_by:
			return (self.num_of_referrals * const.REFERRAL_CREDIT) + const.REFERRAL_CREDIT
		else:
			return self.num_of_referrals * const.REFERRAL_CREDIT


	def __str__(self):
		return self.user.email

	def seller_has_stripe(self, seller):
		if payments.models.Stripe.objects.filter(user=seller).count() == 1:
			stripe.api_key = settings.STRIPE_SECRET_KEY
			
			seller_stripe_obj = payments.models.Stripe.objects.get(user=seller)

			seller_stripe_acc = stripe.Account.retrieve(seller_stripe_obj.stripe_account_id)

			if seller_stripe_acc.charges_enabled == False:
				stripe_enabled = False
				return seller_stripe_obj, stripe_enabled
			
			elif seller_stripe_acc.charges_enabled == True:
				stripe_enabled = True
				return seller_stripe_obj, stripe_enabled
		else: 
			stripe_enabled = False
			seller_stripe_obj = None
			return seller_stripe_obj, stripe_enabled

	
	def has_stripe(self):
		obj = payments.models.Stripe.objects.filter(user=self)
		if obj.count() > 0:
			return mark_safe('<p>Available</p>') 
		return mark_safe('<p>Unavailable</p>')

	def seller_has_stripe(self, seller):
		if payments.models.Stripe.objects.filter(user=seller).count() == 1:
			stripe.api_key = settings.STRIPE_SECRET_KEY
			
			seller_stripe_obj = payments.models.Stripe.objects.get(user=seller)

			seller_stripe_acc = stripe.Account.retrieve(seller_stripe_obj.stripe_account_id)

			if seller_stripe_acc.charges_enabled == False:
				stripe_enabled = False
				return seller_stripe_obj, stripe_enabled
			
			elif seller_stripe_acc.charges_enabled == True:
				stripe_enabled = True
				return seller_stripe_obj, stripe_enabled
		else: 
			stripe_enabled = False
			seller_stripe_obj = None
			return seller_stripe_obj, stripe_enabled
	
	class Meta:
		ordering = ['-user__date_joined']	

class CreditDonation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	donation_amount = models.IntegerField(default=0, blank=False)
	date_donated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.email} donated {self.donation_amount} on {self.date_donated}"


class Location(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	country = models.TextField(blank=True)
	city = models.TextField(blank=True)


class UserFollowing(models.Model):
	user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
	following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		unique_together = ["user_id", "following_user_id"]

	def __str__(self):
		return f"{self.user_id} follows {self.following_user_id}"




class Category(models.Model):
	category_name = models.CharField(max_length=50, blank=False)
	category_val = models.CharField(max_length=50, blank=False)
	image = models.ImageField(upload_to=path_edit_category_img, blank=True)

	def __str__(self):
		return self.category_name
 

class SubCategory(models.Model):
	subcategory_name = models.CharField(max_length=50, blank=False)
	subcategory_val = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.subcategory_name

class Style(models.Model):
	style_name = models.CharField(max_length=50, blank=False)
	style_value = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.style_name


class Material(models.Model):
	material_name = models.CharField(max_length=50, blank=False)
	material_value = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.material_name


class ReferralTransit(models.Model):
	customer = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	dop = models.DateTimeField(default=datetime.now, blank=False)
	completed = models.BooleanField(default=False)
	total_price = models.IntegerField(default=0, blank=False)


#uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid4())).hex[:8]

class HeaderImage(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	header_image = models.ImageField(upload_to=path_edit_header_img, blank=False)

	def __str__(self):
		return self.user.username

class ArtistStatement(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	statement = models.CharField(max_length=2000, blank=False)

	def __str__(self):
		return self.user.username

class FeaturedWork(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150, blank=False)
	description = models.CharField(max_length=2000, blank=True)
	art_image = models.ImageField(upload_to=path_edit_featured_work, blank=False)

	def __str__(self):
		return self.user.username

class Education(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	school = models.CharField(max_length=150, blank=False)
	degree = models.CharField(max_length=150, blank=False)
	field_of_study = models.CharField(max_length=150, blank=False)
	start_year = models.IntegerField(blank=True)
	end_year = models.IntegerField(blank=True)
	description = models.CharField(max_length=2000, blank=True)

	def __str__(self):
		return self.user.username

class Interest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	interests = models.CharField(max_length=2000, blank=True)

	def __str__(self):
		return self.user.username

class Skill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	skills = models.CharField(max_length=2000, blank=True)

	def __str__(self):
		return self.user.username

class Accomplishment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	accomplishment_type = models.CharField(max_length=50, blank=False)
	title = models.CharField(max_length=500, blank=False)
	description = models.CharField(max_length=2000, blank=True)
	link = models.CharField(max_length=500, blank=True)
	month = models.IntegerField(blank=True)
	year = models.IntegerField(blank=True)

	def __str__(self):
		return self.user.username

class Exhibition(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150, blank=False)
	location = models.CharField(max_length=150, blank=True)
	description = models.CharField(max_length=2000, blank=True)
	link = models.CharField(max_length=500, blank=True)
	month = models.IntegerField(blank=True)
	year = models.IntegerField(blank=True)

	def __str__(self):
		return self.user.username


class FollowCategory(models.Model):
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

class TermsAndConditions(models.Model):
	content = models.TextField(blank=True)
	date = models.DateTimeField(default=datetime.now, blank=True)
