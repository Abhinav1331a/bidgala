from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings
from .models import UserPreference, UserPreferenceCategory, UserPreferenceStyle, AdvisoryPageData
from accounts import email_marketing
from accounts.email import create_message, sendgrid_send_email, create_attachment, read_image
from .email_template import surveyCompleteTemplate
import logging
import json




def survey(request, q=''):
	""" This method is used to render the survey page.

	Args:
		request: The request object.

	Returns:
		It renders the survey.html page.

	"""
	return render(request, 'pages/survey.html')


def submitAdvisoryData(request):
	try:
		

		data = json.loads(list(request.POST.keys())[0])
		category_sculpture = False
		category_photography = False
		category_drawing = False
		category_painting = False

		style_abstract = False
		style_blackAndWhite= False
		style_figurative = False
		style_landscape = False
		style_minimalist = False
		style_popArt = False
		style_portraiture = False
		style_street = False
		style_other = False

		orientation_horizontal = False
		orientation_vertical = False
		orientation_square = False

		size_oversize = False
		size_large = False
		size_medium = False
		size_small = False

		firstName = ''
		lastName = ''
		email = ''
		phone = ''
		notes = ''

		budget = 1000

		if data['categories'].get('Drawing', None):
			category_drawing = True

		if data['categories'].get('Painting', None):
			category_painting = True

		if data['categories'].get('Photography', None):
			category_photography = True

		if data['categories'].get('Sculpture', None):
			category_sculpture = True

		if data['styles'].get('Abstract', None):
			style_abstract = True

		if data['styles'].get('Black and White', None):
			style_blackAndWhite = True

		if data['styles'].get('Figurative', None):
			style_figurative = True

		if data['styles'].get('Landscape', None):
			style_landscape = True		

		if data['styles'].get('Minimalist', None):
			style_minimalist = True	

		if data['styles'].get('Pop Art', None):
			style_popArt = True	

		if data['styles'].get('Portraiture', None):
			style_portraiture = True	

		if data['styles'].get('Street', None):
			style_street = True	

		if data['styles'].get('Other', None):
			style_other = True	


		if data['orientation'].get('vertical', None):
			orientation_vertical = True

		if data['orientation'].get('horizontal', None):
			orientation_horizontal = True

		if data['orientation'].get('square', None):
			square = True

		if data['size'].get('small', None):
			size_small = True

		if data['size'].get('medium', None):
			size_medium = True

		if data['size'].get('large', None):
			size_large = True

		if data['size'].get('oversize', None):
			size_oversize = True

		preferred_pieces = str([key for key in data['pieces'].keys() if data['pieces'][key] == True])
		budget = int(float(data['budget']))
		firstName = data['details'].get('firstName', '')
		lastName = data['details'].get('lastName', '')
		email = data['details'].get('email', '')
		phone = data['details'].get('phone', '')
		notes = data['additional'].get('notes', '')

		newsletterSubscription = data['additional'].get('newsletterSubscription', False)

		if newsletterSubscription:
			try:
				email_marketing.registerMailChimp(email, firstName, lastName)
			except Exception as e:
				print(e)
				logging.getLogger("error_logger").error(str(e))

		if AdvisoryPageData.objects.filter(email=email).count() >= 0:
			model = AdvisoryPageData(category_sculpture=category_sculpture, category_photography=category_photography, \
				category_drawing=category_drawing, category_painting=category_painting, style_abstract=style_abstract, \
				style_blackAndWhite=style_blackAndWhite, style_figurative=style_figurative, style_landscape=style_landscape, \
				style_minimalist=style_minimalist, style_popArt=style_popArt, style_portraiture=style_portraiture, \
				style_street=style_street,style_other=style_other, preferred_pieces=preferred_pieces,\
				orientation_horizontal=orientation_horizontal, orientation_vertical=orientation_vertical, \
				orientation_square=orientation_square, size_oversize=size_oversize, size_large=size_large,\
				size_medium=size_medium, size_small=size_small, budget=budget, firstName=firstName, lastName=lastName,\
				email=email, phone=phone, notes=notes, newsletterSubscription=newsletterSubscription)
			model.save()
			response = {
			'status' : 'fail',
			'message' : 'Thank you for submitting',
			}
			status_code = 200

			try:

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

				subject = 'Art advisory'
				
				attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
				
				attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
				attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
				attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
				attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
				attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')

				message_ = create_message(email, subject, surveyCompleteTemplate(firstName))

				message_.add_attachment(attachment1)
				message_.add_attachment(attachment_facebook)
				message_.add_attachment(attachment_twitter)
				message_.add_attachment(attachment_instagram)
				message_.add_attachment(attachment_linkedin)
				message_.add_attachment(attachment_pinterest)

				sendgrid_send_email(message_)
			except Exception as e:
				logging.getLogger("error_logger").error(str(e))

			try:
				None
			except Exception as e:
				logging.getLogger("error_logger").error(str(e))

			try:
				message = 'Name: {}<br>category_sculpture: {}<br>category_photography: {}<br>category_drawing: {}<br>\
							category_painting: {}<br>style_abstract: {}<br>style_blackAndWhite: {}<br>\
							style_figurative: {}<br>style_landscape: {}<br>style_minimalist: {}<br>style_popArt: {}<br>\
							style_portraiture: {}<br>style_street: {}<br>style_other: {}<br>orientation_horizontal: {}<br> \
							orientation_vertical: {}<br>orientation_square: {}<br>size_oversize: {}<br>size_large:{}<br> \
							size_medium: {}<br>size_small: {}<br>email: {}<br>phone: {}<br>budget: {}<br>notes: {}<br>'\
							.format(firstName + ' ' + lastName, \
								category_sculpture, \
								category_photography, \
								category_drawing, \
								category_painting, \
								style_abstract, \
								style_blackAndWhite, \
								style_figurative, \
								style_landscape, \
								style_minimalist,\
								style_popArt, \
								style_portraiture, \
								style_street, \
								style_other, \
								orientation_horizontal, \
								orientation_vertical, \
								orientation_square,\
								size_oversize,\
								size_large, \
								size_medium, \
								size_small, \
								email, \
								phone, \
								budget, \
								notes
								)
				send_bidgala = create_message('info@bidgala.com', 'Quiz survey', message)
				sendgrid_send_email(send_bidgala)
				
			except Exception as e:
				logging.getLogger("error_logger").error(str(e))

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))

		response = {
			'status' : 'fail',
			'message' : 'Something went wrong! Please try again later',
		}
		status_code = 500	
		
	return JsonResponse(response, status=status_code)

def getUserPreferenceOptions(request):
	""" This method is used to return the user preference json.

	Args:
		request: The request object.

	Returns:
		JSON object.

	"""
	obj = UserPreference.objects.all().values()
	response = {'result' : list(obj), 'img_host_url' : settings.BASE_AWS_IMG_URL, 'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM, }
	return JsonResponse(response, safe=False)

def getUserPreferenceCategoryOptions(request):
	""" This method is used to return the category preference json.

	Args:
		request: The request object.

	Returns:
		JSON object.

	"""
	obj = UserPreferenceCategory.objects.all().values()
	response = {'result' : list(obj), 'img_host_url' : settings.BASE_AWS_IMG_URL, 'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM, }
	return JsonResponse(response, safe=False)

def getUserPreferenceStyleOptions(request):
	""" This method is used to return the style preference json.

	Args:
		request: The request object.

	Returns:
		JSON object.

	"""
	obj = UserPreferenceStyle.objects.all().values()
	response = {'result' : list(obj), 'img_host_url' : settings.BASE_AWS_IMG_URL, 'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM, }
	return JsonResponse(response, safe=False)
