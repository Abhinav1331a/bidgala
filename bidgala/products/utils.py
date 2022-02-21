from django.core.files.base import ContentFile
from django.conf import settings
from django.db.models import Q
import base64
import six
import uuid
import imghdr
from django.core.paginator import Paginator


import stripe

from accounts.models import UserInfo
from accounts import choices
from products import choices as product_choices
from .models import WishlistProduct, Product
from accounts.models import UserInfo
import accounts.choices as choices

def display(request):
	product_object = Product.objects.order_by('-date').filter(owner=UserInfo.objects.get(user = request.user.id), available=True)
	paginator = Paginator(product_object, 50)
	page = request.GET.get('page')
	paged_arts = paginator.get_page(page)
	context = {}
	if len(paged_arts) > 0:
		context['arts'] = paged_arts
		context['category'] = product_choices.category
		context['style'] = product_choices.styles
		context['material'] = product_choices.material
		context['dim_measurement'] = product_choices.dim_measurement
		context['is_single_image'] = True if product_object.count() == 1 else False

	return context


def is_number(val):
	""" This method is used to check if a input is 
	number or not.

	Args:
		val: The string value

	Returns:
		True if no exception else False.
	"""
	try:
		temp = float(val)
		return True
	except Exception as e:
		return False


def get_stripe_customer(user):
	stripe.api_key = settings.STRIPE_SECRET_KEY

	customer_id = user.stripe_customer_id

	stripe_customer = stripe.Customer.retrieve(customer_id)
	stripe_customer_payment_methods = stripe.PaymentMethod.list(customer=customer_id, type="card")


	return stripe_customer, stripe_customer_payment_methods

def is_user_wish_list_product(user_info_obj, product_obj):
	""" This is a helper function to check if the user put an item in wishlist
	"""
	criterion1 = Q(user=user_info_obj)
	criterion2 = Q(product=product_obj)
	obj = WishlistProduct.objects.filter(criterion1 & criterion2)
	return True if obj.count() > 0 else False
		

def get_user_wish_list_products(user_info_obj):
	""" This is a helper function to retrive the  user wishlist items
	"""
	temp = []
	for each_wish_list in WishlistProduct.objects.filter(user=user_info_obj):
		temp.append(str(each_wish_list.product.id))
	return temp




def decode_base64_file(data, sub_name=None):

    def get_file_extension(file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:5] # 5 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        if sub_name is None:
            complete_file_name = "%s.%s" % (file_name, file_extension, )
        else:
             complete_file_name = "%s.%s" % (file_name + sub_name, file_extension, )

        return ContentFile(decoded_file, name=complete_file_name)