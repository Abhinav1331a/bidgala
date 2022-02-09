from django.db import models
from django.utils.html import mark_safe
from django.conf import settings
from datetime import datetime
import uuid
import requests
import logging
import base64

from accounts.models import Category
from accounts.models import SubCategory
from accounts.models import Style
from accounts.models import UserInfo
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email
from accounts import email_template


def path_edit(instance, filename):
	return '/'.join(['products', str(instance.category.id),
		str(instance.subcategory.id), str(instance.id) + '_' +  filename])

# Create your models here.
class Product(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	art_title = models.CharField(max_length=100, blank=False)
	art_desc = models.TextField(blank=False, default='')
	tags = models.TextField(blank=True)
	height = models.FloatField(default=0)
	depth = models.FloatField(blank=True, null=True)
	width = models.FloatField(default=0)
	dim_measure = models.CharField(blank=True, max_length=20)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

	price = models.IntegerField(blank=False, default=0)
	shipping_price_us = models.IntegerField(blank=False, default=0)
	shipping_price_can = models.IntegerField(blank=False, default=0)
	shipping_price_uk = models.IntegerField(blank=False, default=0)
	shipping_price_asia = models.IntegerField(blank=False, default=0)
	shipping_price_aunz = models.IntegerField(blank=False, default=0)
	shipping_price_europe = models.IntegerField(blank=False, default=0)
	shipping_price_other = models.IntegerField(blank=False, default=0)

	show_shipping_price_us = models.BooleanField(blank=False, default=True)
	show_shipping_price_can = models.BooleanField(blank=False, default=True)
	show_shipping_price_uk = models.BooleanField(blank=False, default=True)
	show_shipping_price_asia = models.BooleanField(blank=False, default=True)
	show_shipping_price_aunz = models.BooleanField(blank=False, default=True)
	show_shipping_price_europe = models.BooleanField(blank=False, default=True)
	show_shipping_price_other = models.BooleanField(blank=False, default=True)

	color = models.CharField(max_length=20, blank=False)
	color_1 = models.CharField(max_length=20, blank=True)
	color_2 = models.CharField(max_length=20, blank=True)
	color_3 = models.CharField(max_length=20, blank=True)
	color_4 = models.CharField(max_length=20, blank=True)

	owner = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now, blank=True)
	image = models.ImageField(upload_to=path_edit, blank=False)
	additional_image_1 = models.ImageField(upload_to=path_edit, blank=True)
	additional_image_2 = models.ImageField(upload_to=path_edit, blank=True)
	additional_image_3 = models.ImageField(upload_to=path_edit, blank=True)
	additional_image_4 = models.ImageField(upload_to=path_edit, blank=True)

	sold = models.BooleanField(default=False, blank=True)
	available = models.BooleanField(default=True, blank=True)

	is_signed = models.BooleanField(blank=True, null=True)
	is_framed_or_hang = models.CharField(blank=True, null=True, max_length=5)
	styles = models.TextField(blank=True, null=True)
	materials = models.TextField(blank=True, null=True)

	curator_pick = models.BooleanField(default=False, blank=True)
	home_decor = models.BooleanField(default=False, blank=True)
	structube = models.BooleanField(default=False, blank=True)

	comment_count = models.PositiveIntegerField(default=0)
	favourite_count = models.PositiveIntegerField(default=0)


	def save(self, *args, **kwargs):
		if self.id:
			cls = self.__class__
			old = cls.objects.filter(id=self.id)
			if old.count() > 0:
				new = self
				changed_fields = []
				old = old[0]

				for field in cls._meta.get_fields():
					if field.__class__.__name__ != 'ManyToOneRel':
						field_name = field.name
						try:
							if getattr(old, field_name) != getattr(new, field_name):
								changed_fields.append(field_name)
						except Exception as ex:
							logging.getLogger("error_logger").error(str(ex))

				if 'curator_pick' in changed_fields:

					kwargs['update_fields'] = changed_fields
					
					if (old.curator_pick != new.curator_pick) and (new.curator_pick) and (new.sold == False) and (new.available == True):
						customer_name = old.owner.user.first_name + ' ' + old.owner.user.last_name

						from_email = settings.FROM_EMAIL
						to_email = old.owner.user.email
						subject='Notification on your curator pick'

						title_of_art = new.art_title
						price_of_art = new.price
						dim_of_art = str(new.height) + ' x ' + str(new.width)
						if old.depth:
							dim_of_art = dim_of_art + ' x ' + str(new.depth)

						dim_of_art = dim_of_art + ' ' + new.dim_measure

						# IMAGE URL
						img_url = settings.HOST_BASE_URL + 'art/product_view/' + str(new.id) + '/'

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
						message_ = create_message(to_email, subject, email_template.receiveCuratorPicks(customer_name, title_of_art, price_of_art, dim_of_art, img_url))

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

					else:
						new.curator_pick = False

		super().save(*args, **kwargs)

	def main_image(self):
		return mark_safe('<a target="_blank" download="%s" href="https://thebidgala-prod.s3.amazonaws.com/%s"><img src="https://thebidgala-prod.s3.amazonaws.com/%s"  style="width:150px; height:150px" alt="No Image to preview"/></a' % (self.art_title, self.image, self.image))

	def additional_1_view(self):
		return mark_safe('<a target="_blank" download="%s" href="https://thebidgala-prod.s3.amazonaws.com/%s" ><img src="https://thebidgala-prod.s3.amazonaws.com/%s"  style="width:150px; height:150px" alt="No Image to preview" /></a>' % (self.art_title+'_1', self.additional_image_1, self.additional_image_1))

	def additional_2_view(self):
		return mark_safe('<a target="_blank" download="%s" href="https://thebidgala-prod.s3.amazonaws.com/%s" ><img src="https://thebidgala-prod.s3.amazonaws.com/%s"  style="width:150px; height:150px" alt="No Image to preview" /></a>' % (self.art_title+'_2', self.additional_image_2, self.additional_image_2))

	def additional_3_view(self):
		return mark_safe('<a target="_blank" download="%s" href="https://thebidgala-prod.s3.amazonaws.com/%s" ><img src="https://thebidgala-prod.s3.amazonaws.com/%s"  style="width:150px; height:150px" alt="No Image to preview" /></a>' % (self.art_title+'_3', self.additional_image_3, self.additional_image_3))

	def additional_4_view(self):
		return mark_safe('<a target="_blank" download="%s" href="https://thebidgala-prod.s3.amazonaws.com/%s" ><img src="https://thebidgala-prod.s3.amazonaws.com/%s"  style="width:150px; height:150px"" alt="No Image to preview" /></a>' % (self.art_title+'_4', self.additional_image_4, self.additional_image_4))


class WishlistProduct(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now, blank=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=50000, blank=True)
    user =  models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="product_comment_user")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)
    parent =  models.TextField(null=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
