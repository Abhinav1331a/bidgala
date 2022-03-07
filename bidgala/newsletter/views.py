from bidgala.local_settings import HOST_BASE_URL
from . import email_template
from multiprocessing import context
from django.shortcuts import render 
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.http import HttpResponse, JsonResponse
import logging
from .models import NewsletterUser
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email
from accounts.utils import random_string, encrypt, decrypt
from password import constants as const
from urllib.parse import unquote



def NewsLetter(request):
    if request.method == 'POST':
        
        email_input = request.POST.get('email_value')
        exists = NewsletterUser.objects.filter(email=email_input).first()
        if exists is not None:
            exists_confirmed = NewsletterUser.objects.get(id = exists.id).confirmed
            if exists_confirmed:
                data = 'This email is already subscribed! <br><br> Reload the page and try again to subscribe with a new email.'
                return HttpResponse(data)
            else:
                b = NewsletterUser.objects.get(id = exists.id)
                b.confirmed = True
                b.save()
                sendEmail(email_input)  
                data = 'Thank you for subscribing! <br><br> You will now receive updates about our latest collections regularly!'
                return HttpResponse(data)
        else:
            new = NewsletterUser(email=email_input, confirmed = True)
            new.save()
            sendEmail(email_input)            
            data = 'Thank you for subscribing! <br><br> You will now receive updates about our latest collections regularly!'
            return HttpResponse(data)


def sendEmail(email):
    
    is_receipt = False
    from_email = settings.FROM_EMAIL
    to_email = email
    subject='BIDGALA DIGEST'

    IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
    data1 = read_image(IMG_1_PATH)
    
    message_ = create_message(to_email, subject, email_template.NewsLetterSubscribedTemplate(email))
        
    attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')

    if not is_receipt:
        message_.add_attachment(attachment1)

    sendgrid_send_email(message_)
        
    
def CancelSubscription(request):
    return render(request, "newsletter/CancelSubscription.html")

def DeleteNewsLetter(request):
    if request.method == 'POST':
        del_id = request.POST.get('id_value')
        deciper_text = str(decrypt(const.SECRET_KEY, unquote(del_id)), 'utf-8')
        data = deciper_text.split(':')
        unsubscribe = NewsletterUser.objects.filter(id= data[0]).first()
        unsubscribe.confirmed = False
        unsubscribe.save()
    return render(request, "newsletter/CancelSubscription.html")
