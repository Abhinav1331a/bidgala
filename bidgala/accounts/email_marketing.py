# Standard library imports
from django.conf import settings
import hashlib

# Related third party imports
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Local application/library specific imports



def registerMailChimp(email, firstName='', lastName=''):
	mailchimp = MailchimpMarketing.Client()
	mailchimp.set_config({
	  "api_key": settings.MAILCHIMP_API_KEY,
	  "server": settings.MAILCHIMP_DATA_CENTER
	})

	list_id = settings.MAILCHIMP_EMAIL_LIST_ID
	member_info = {
	    "email_address": email,
	    "status": "subscribed",
	    "merge_fields": {
	      "FNAME": firstName,
	      "LNAME": lastName
    }
    }
	response_code_for_add = mailchimp.lists.add_list_member(list_id, member_info)

	

def updateTagMailChimp(email, tag=''):
	mailchimp = MailchimpMarketing.Client()
	mailchimp.set_config({
	  "api_key": settings.MAILCHIMP_API_KEY,
	  "server": settings.MAILCHIMP_DATA_CENTER
	})
	list_id = settings.MAILCHIMP_EMAIL_LIST_ID
	SUBSCRIBER_HASH = hashlib.md5(email.encode('utf-8')).hexdigest()
	response = mailchimp.lists.update_list_member_tags(list_id, SUBSCRIBER_HASH, body={
        "tags": [{
            "name": tag,
            "status": "active"
        }]
    })
