import base64
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)


def create_message(to_email, subject, html_content, from_email=settings.FROM_EMAIL):
	""" This method is used to create a message object provided by the 
		sendgrid api.

		Args:
		from_email: This is the user email address
		subject: subject of the email
		html_content: The html content that needs to be embedded into an email
		from_email: By default, it is the bidgala email address
	
		Returns:
		It returns sendgrid message object
	""" 
	message = Mail(
			   		from_email=(from_email, 'Bidgala'),
			    	to_emails=to_email,
			   		subject=subject,
			 		html_content=html_content
			 		)
	return message

def create_attachment(raw_data, file_type, file_name, content_id ,disposition='inline'):
	""" This method is used to create a attachment object provided by the 
		sendgrid api.

		Args:
		raw_data: This is the binary data of the image
		plaintext: message to be encrypted
	
		Returns:
		It returns sendgrid message object
	"""
	attachment = Attachment()
	file_content = base64.b64encode(raw_data).decode()
	attachment.file_content = FileContent(file_content)
	attachment.file_type = FileType(file_type)
	attachment.file_name = FileName(file_name)
	attachment.disposition = Disposition(disposition)
	attachment.content_id = ContentId(content_id)
	return attachment


def read_image(file_name):
	""" This method is used to read the image and produce the binary data

		Args:
		file_name: Path of the image

		Returns:
		It returns the image binary data
	"""
	data = None
	with open(file_name, 'rb') as f:
		data = f.read()
		f.close()
	return data 


def sendgrid_send_email(message_obj):
	""" This method is used to send an email using sendgrid api

		Args:
		message_obj: The passed object is already added with attachments (important)

		Returns:
		None
	"""
	sendgrid_api_key = settings.SENDGRID_API_KEY
	sg = SendGridAPIClient(sendgrid_api_key)
	sg.send(message_obj)
