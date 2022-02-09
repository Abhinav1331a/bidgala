# Standard library imports
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.http import JsonResponse

# Related third party imports


# Local application/library specific imports
from accounts import choices
from products import choices as product_choices
from accounts.models import UserInfo, TermsAndConditions
from products.models import Product
from discover.models import Article
from .models import HomePage
from .utils import get_featured_artist, get_category, get_channel
from products import choices as product_choices



def cookie(request):
	""" This method is used to render the cookie page.

	Args:
		request: The request object.

	Returns:
		It renders the cookie.html page.

	"""

	return render(request, 'pages/cookie.html')



def directory(request):
	""" This method is used to render the directory page.

	Args:
		request: The request object.

	Returns:
		It renders the directory.html page.

	"""
	pro = UserInfo.objects.filter(is_professional=True, company_email_verified=True)
	
	context = {
	'profession' : choices.professions,
	'country':choices.country,
	'professional' : pro
	}

	return render(request, 'directory/directory.html', context)


def partners(request):
	""" This method is used to render the partners page.

	Args:
		request: The request object.

	Returns:
		It renders the partners.html page.

	"""

	return render(request, 'partners/partners.html')


def privacy(request):
	""" This method is used to render the privacy page.

	Args:
		request: The request object.

	Returns:
		It renders the privact.html page.

	"""

	return render(request, 'pages/privacy.html')


def bidgala_101(request):
	""" This method is used to render the bidgala101 page.

	Args:
		request: The request object.

	Returns:
		It renders the bidgala101.html page.

	"""
	return render(request, "pages/bidgala101.html", {'category' : product_choices.category,})


def terms_of_conditions(request):
	return render(request, "pages/tos.html")


def index(request):
	""" This method is used to render the index page.

	Args:
		request: The request object.

	Returns:
		It renders the index.html page.

	"""


	products = Product.objects.filter(curator_pick=True, sold=False, available=True).order_by('-date')[0:10]
	new_products = Product.objects.filter(sold=False, available=True).order_by('-date').distinct('owner__id').order_by('owner__id')[0:10]
	discover_articles = Article.objects.filter(show=True).order_by('-created_date')[0:10]

	all_art_img  = HomePage.objects.filter(value='shop_all_art')[0]
	advisory_img  = HomePage.objects.filter(value='advisory')[0]

	channel_obj = get_channel()
	featured_artist = get_featured_artist()

	featured_artist_art = []

	for i in featured_artist:
		temp_data = Product.objects.filter(owner=i).order_by('-date')

		if temp_data.count() >= 1:
			featured_artist_art.append(temp_data[0])

	category_obj = get_category()
	context = {
	'all_art_img' : all_art_img.image,
	'advisory_img' : advisory_img.image,
	'discover_articles': discover_articles,
	'category' : product_choices.category,
	'subcategory' : product_choices.subcategory,
	'products' : products,
	'channels' : channel_obj,
	'featured_artists' : featured_artist_art,
	'new_products' : new_products,
	'category_objs' : category_obj,
	'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
	'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
	}

	return render(request, 'pages/index.html', context)


def index_demo(request):
	""" This method is used to render the index page with context
	for demo.

	Args:
		request: The request object.

	Returns:
		It renders the index.html page.

	"""
	#products = Product.objects.filter(curator_pick=True).order_by('-date')[0:10]
	#new_products = Product.objects.filter(curator_pick=False).filter(available=True).filter(sold=False).order_by('-date')[0:10]
	#channel_obj = get_channel()
	#featured_artist = get_featured_artist()
	products = Product.objects.filter(curator_pick=True, sold=False, available=True).order_by('-date')[0:10]
	new_products = Product.objects.filter(sold=False, available=True).order_by('-date').distinct('owner__id').order_by('owner__id')[0:10]
	discover_articles = Article.objects.filter(show=True).order_by('-created_date')[0:10]

	channel_obj = get_channel()
	featured_artist = get_featured_artist()

	featured_artist_art = []

	for i in featured_artist:
		temp_data = Product.objects.filter(owner=i).order_by('-date')

		if temp_data.count() > 0:
			featured_artist_art.append(temp_data[0])

			
	category_obj = get_category()

	context = {
		'demo' : True,
		'discover_articles': discover_articles,
		'category' : product_choices.category,
		'subcategory' : product_choices.subcategory,
		'new_products' : new_products,
		'featured_artists' : featured_artist_art,
		'channels' : channel_obj,
		'products' : products,
		#'products' : products,
		#'channels' : channel_obj,
		#'featured_artists' : featured_artist,
		#'new_products' : new_products,
		'category_objs' : category_obj,
		'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
		'category' : product_choices.category,
		'img_optimize_param_large' : settings.IMG_OPTIMIZE_PARAM_LARGE,
		'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
		#'toc' : TermsAndConditions.objects.all().order_by('-date')[0]
	}
	return render(request, 'pages/index.html', context)


def about(request):
	""" This method is used to render the about page.

	Args:
		request: The request object.

	Returns:
		It renders the about.html page.

	"""
	
	return render(request, 'pages/about.html')



def coming_soon(request):
	""" This method is used to render the coming soon page.

	Args:
		request: The request object.

	Returns:
		It renders the coming_soon.html page.

	"""
	# Just in case if session does not get deleted, the do not display
	# old messages.
	request.messages = None
	return render(request, 'pages/coming_soon.html')


def pack_guide(request):
	""" This method is used to render the packaging guide page.

	Args:
		request: The request object.

	Returns:
		It renders the guide page.

	"""
	# Just in case if session does not get deleted, the do not display
	# old messages.
	request.messages = None
	return render(request, 'pages/guide.html')


def error_404(request, exception):
	""" This method is used to render the 404 error page.

	Args:
		request: The request object.

	Returns:
		It renders the error_404.html page.

	"""
	return render(request, "error/error_404.html")


def error_500(request):
	""" This method is used to render the 500 error page.

	Args:
		request: The request object.

	Returns:
		It renders the error_500.html page.

	"""
	return render(request, "error/error_500.html")


def terms_of_service(request):
	""" This method is used to render the terms of service page.

	Args:
		request: The request object.

	Returns:
		It renders the terms_of_service.html page.

	"""
	return render(request, 'pages/terms_of_service.html')

def help(request):
	""" This method is used to render the help page.

	Args:
		request: The request object.

	Returns:
		It renders the help.html page.

	"""
	return render(request, 'pages/help.html')

def faq(request):
	""" This method is used to render the faq page.

	Args:
		request: The request object.

	Returns:
		It renders the faq.html page.

	"""
	return render(request, 'pages/faq.html')

def advisory(request):
	""" This method is used to render the advisory page.

	Args:
		request: The request object.

	Returns:
		It renders the advisory.html page.

	"""
	return render(request, 'pages/advisory.html')




