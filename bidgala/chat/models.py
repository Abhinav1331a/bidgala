# Standard library imports
from django.db import models
from django.conf import settings
from datetime import datetime
from encrypted_fields import fields
import logging
import base64
import uuid


# Local application/library specific imports
from .email_template import sendEmail
from accounts.models import UserInfo
from payments.models import OrderHold
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email



class  ConversationManager(models.Manager):
	"""This is used to check if both the users had already had a conversation or not.
		Incase, if there is not previous conversation then we create new tuple else reeturn old one
		user is a auth_USER object
		other_user is a String which represents the ID in UserInfo table.
	"""
	def get_or_create(self, user, other_user):
		try:
			user_obj = UserInfo.objects.filter(user=user)
			other_user_obj = UserInfo.objects.filter(id=other_user)
			if (other_user_obj.count() == 0) or (other_user_obj[0].user == user) or (user_obj.count() == 0):
				return None, False


			query_1 = self.get_queryset().filter(user_1 = user_obj[0], user_2=other_user_obj[0])
			query_2 = self.get_queryset().filter(user_2 = user_obj[0], user_1=other_user_obj[0])


			if query_1.count() + query_2.count() == 1:
				if query_1.count() == 1:
					return query_1.first(), False
				else:
					return query_2.first(), False
			else:

				new_obj = self.model(user_1=user_obj[0], user_2=other_user_obj[0])
				new_obj.save()
				return new_obj, True

		except Exception as e:
			logging.getLogger("error_logger").error(str(e))
			return None, False


class  MessageManager(models.Manager):
	""" This class is used to stoere the message in db. It also sends an email for every message it stores.
	"""
	def store(self, conversation_id, message_from, message):
		try:
			conversation_obj = Conversation.objects.get(id=conversation_id)
			user_obj = UserInfo.objects.get(id=message_from)
			new_obj = self.model(message_text=message, conversation_id=conversation_obj, origin_user=user_obj)
			new_obj.save()

			try:

				from_email = settings.FROM_EMAIL

				to_user_conv = None

				if str(conversation_obj.user_1.id) != str(user_obj.id):
					to_user_conv = conversation_obj.user_1
				else:
					to_user_conv = conversation_obj.user_2

				to_email = to_user_conv.user.email
				from_username = user_obj.user.username
				from_user_id = str(user_obj.id)

				subject='New Reply from ' + from_username

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

				message_ = create_message(to_email, subject, sendEmail(message, from_username, from_user_id))

				attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
				attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
				attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
				attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
				attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
				attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')

				# encoded1 = base64.b64encode(data1).decode()
				# attachment1 = Attachment()
				# attachment1.file_content = FileContent(encoded1)
				# attachment1.file_type = FileType('img/png')
				# attachment1.file_name = FileName('logo.png')
				# attachment1.disposition = Disposition('inline')
				# attachment1.content_id = ContentId('logo')

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

			return new_obj, True
		except Exception as e:
			logging.getLogger("error_logger").error(str(e))
			return None, False

	def ack_message(self, ack_user, message_id):
		try:
			obj = self.get_queryset().get(id=message_id)
			if str(obj.conversation_id.user_1.id) == ack_user or str(obj.conversation_id.user_2.id) == ack_user:
				if str(obj.origin_user.id) != ack_user:
					obj.read = True
					obj.save()
					return True
			return False
		except Exception as e:
			logging.getLogger("error_logger").error(str(e))
			return False


class Conversation(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	user_1 = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_1')
	user_2 = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_2')
	created_date = models.DateTimeField(default=datetime.now, blank=True)
	objects = ConversationManager()

	def __str__(self):
		return str(self.id)



class Message(models.Model):
	message_text = fields.EncryptedTextField(blank=True, null=True)
	conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
	origin_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, blank=False, default=None)
	timestamp = models.DateTimeField(default=datetime.now, blank=True)
	read = models.BooleanField(default=False)
	order_hold =  models.ForeignKey(OrderHold, default=None, null=True, on_delete=models.CASCADE)
	has_input = models.BooleanField(default=False)
	buyer_notify_msg = models.BooleanField(default=False)
	objects = MessageManager()

	def __str__(self):
		return self.message_text
