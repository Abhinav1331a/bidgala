from django.db import models
from datetime import datetime
from accounts.models import UserInfo
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from accounts.utils import random_string, encrypt, decrypt
from password import constants as const
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email

# Create your models here.

class NewsletterUser(models.Model):
    email = models.EmailField(null=True)
    confirmed = models.BooleanField(null=True)
    date_added =  models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.email


class NewsletterContent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='newsletter/media')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = NewsletterUser.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:

            confirmation_str = random_string()
            user_id = str(sub.id)
            encrypted_text = str(encrypt(const.SECRET_KEY, user_id + ':' + confirmation_str) ,'utf-8')
        
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}/CancelSubscription?{}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/newsletter'),
                            encrypted_text)
                    )

            IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
            IMG_2_PATH = settings.BASE_DIR + '/bidgala/static/img/email/bottom.jpg'
            data1 = read_image(IMG_1_PATH)
            data2 = read_image(IMG_2_PATH)
            attachment1 = create_attachment(data1, 'img/jpg', 'logo.jpg', 'logo')
            attachment2 = create_attachment(data2, 'img/jpg', 'bottom.jpg', 'bottom')
            message.add_attachment(attachment1)
            message.add_attachment(attachment2)

            sg.send(message)