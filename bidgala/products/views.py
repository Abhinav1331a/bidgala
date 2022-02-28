# Standard library imports
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.contrib import messages
from django.conf import settings
from django.templatetags.static import static
import json
import io
from django.core.files import File
import logging
import operator
import functools
import numpy as np
from datetime import datetime
import random
import sys
from rest_framework import generics, permissions, filters
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from rest_framework.response import Response

# Related third party imports
import stripe

# Local application/library specific imports
from accounts import constants, choices
from products import choices as product_choices
from accounts.models import UserInfo, Style, Material, SubCategory, Category
from payments.models import Stripe, Orders
from .models import Product, WishlistProduct, Comment
from . import email_template
from products import cached_data
from .utils import decode_base64_file, is_number, get_stripe_customer, get_user_wish_list_products, is_user_wish_list_product, display
from exceptions.customs import InvalidFormatException, NotPostRequestException, PostDataMissingException
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email
from .serializers import ProductSerializer, ProductAndUserSerializer



class CuratorList(generics.ListAPIView):
    serializer_class = ProductSerializer	
    def get_queryset(self):
        max = int(self.request.query_params.get('max', '10'))
        date_order = self.request.query_params.get('dateorder', 'asc')

        if date_order == 'asc':
            filter_date = 'date'
        else:
            filter_date = '-date'
        return Product.objects.filter(curator_pick=True, sold=False, available=True).order_by(filter_date)[0:max]


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAndUserSerializer



class NewArtList(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        max = int(self.request.query_params.get('max', '10'))
        date_order = self.request.query_params.get('dateorder', 'asc')

        if date_order == 'asc':
            filter_date = 'date'
        else:
            filter_date = '-date'
        return Product.objects.filter(sold=False, available=True).order_by(filter_date).distinct('owner__id').order_by('owner__id')[0:max]

@login_required
def art_sold(request):
    """ This method is used to set art as sold in db

    Args:
            request: The request object.

        Returns:
            It redirects to my_art page

    """
    try:
        if request.method == 'POST':
            product_id = request.POST['art_id_sold']
            obj = Product.objects.get(id=product_id)
            obj.sold = True
            obj.save()
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
    return redirect('my_art')

@login_required
def art_unsold(request):
    """ This method is used to set art as sold in db

    Args:
            request: The request object.

        Returns:
            It redirects to my_art page

    """
    try:
        if request.method == 'POST':
            product_id = request.POST['art_id_unsold']
            obj = Product.objects.get(id=product_id)

            # If the product is already registered in orders table, then we cannot make it as unsold
            if Orders.objects.filter(order_hold__product=obj).count() > 0:
                redirect('my_art')

            obj.sold = False
            obj.available = True
            obj.save()
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
    return redirect('my_art')


def filter_art(request):
    """ It is used to filter the arts based on the criteria

        Args:
            request: The request object.

        Returns:
            It return a JSON Object.
    """
    try:

        category = []
        subcategory = []
        style = []
        color_list = []
        min_price = None
        price_factor_above = None

        sort_by = None
        min_price_custom = None
        max_price_custom = None
        width_min = None
        width_max = None
        height_min = None
        height_max = None
        depth_min = None
        depth_max = None
        measurement_unit = None

        width_min_i = 0
        width_max_i = sys.maxsize
        height_min_i = 0
        height_max_i = sys.maxsize
        depth_min_i = 0
        depth_max_i = sys.maxsize

        width_min_m = 0
        width_max_m = sys.maxsize
        height_min_m = 0
        height_max_m = sys.maxsize
        depth_min_m = 0
        depth_max_m = sys.maxsize


        width_min_cm = 0
        width_max_cm = sys.maxsize
        height_min_cm = 0
        height_max_cm = sys.maxsize
        depth_min_cm = 0
        depth_max_cm = sys.maxsize

        # By default we get page one
        if request.POST.get('page', None):
            page = int(request.POST['page'])
        else:
            page = 1

        if(request.POST.get('sort_by', '') in ['lf', 'hf']):
            sort_by = request.POST['sort_by']

        try:
               min_price_custom = int(request.POST.get('min_price_custom', ''))
        except ValueError:
            None

        try:
               max_price_custom = int(request.POST.get('max_price_custom', ''))
        except ValueError:
            None

        try:
               width_min = abs(int(request.POST.get('width_min', '')))
        except ValueError:
            None

        try:
               width_max = abs(int(request.POST.get('width_max', '')))
        except ValueError:
            None

        try:
               height_min = abs(int(request.POST.get('height_min', '')))
        except ValueError:
            None

        try:
               height_max = abs(int(request.POST.get('height_max', '')))
        except ValueError:
            None


        try:
               depth_min = abs(int(request.POST.get('depth_min', '')))
        except ValueError:
            None


        try:
               depth_max = abs(int(request.POST.get('depth_max', '')))
        except ValueError:
            None

        
        if request.POST.get('measurement_unit', '') in ['cm', 'm', 'i']:
            measurement_unit = request.POST['measurement_unit']
            if request.POST['measurement_unit'] == 'm':
                if width_min:
                    width_min_m = width_min
                    width_min_i = 39.3701 * width_min
                    width_min_cm = 100 * width_min

                if width_max:
                    width_max_m = width_max
                    width_max_i = 39.3701 * width_max
                    width_max_cm = 100 * width_max

                if height_min:
                    height_min_m = height_min
                    height_min_i = 39.3701 * height_min
                    height_min_cm = 100 * height_min

                if height_max:
                    height_max_m = height_max
                    height_max_i = 39.3701 * height_max
                    height_max_cm = 100 * height_max

                if depth_min:
                    depth_min_m = depth_min
                    depth_min_i = 39.3701 * depth_min
                    depth_min_cm = 100 * depth_min

                if depth_max:
                    depth_max_m = depth_max
                    depth_max_i = 39.3701 * depth_max
                    depth_max_cm = 100 * depth_max

            elif request.POST['measurement_unit'] == 'cm':
                if width_min:
                    width_min_m = 0.01 * width_min
                    width_min_i = 0.393701 * width_min
                    width_min_cm = width_min

                if width_max:
                    width_max_m = 0.01 * width_max
                    width_max_i = 0.393701 * width_max
                    width_max_cm = width_max

                if height_min:
                    height_min_m = 0.01 * height_min
                    height_min_i = 0.393701 * height_min
                    height_min_cm = height_min

                if height_max:
                    height_max_m = 0.01 * height_max
                    height_max_i = 0.393701 * height_max
                    height_max_cm = height_max

                if depth_min:
                    depth_min_m = 0.01 * depth_min
                    depth_min_i = 0.393701 * depth_min
                    depth_min_cm = depth_min

                if depth_max:
                    depth_max_m = 0.01 * depth_max
                    depth_max_i = 0.393701 * depth_max
                    depth_max_cm = depth_max

            elif request.POST['measurement_unit'] == 'i':
                if width_min:
                    width_min_m = 0.0254 * width_min
                    width_min_i = width_min
                    width_min_cm = 2.54 * width_min

                if width_max:
                    width_max_m = 0.0254 * width_max
                    width_max_i = width_max
                    width_max_cm = 2.54 * width_max

                if height_min:
                    height_min_m = 0.0254 * height_min
                    height_min_i = height_min
                    height_min_cm = 2.54 * height_min

                if height_max:
                    height_max_m = 0.0254 * height_max
                    height_max_i = height_max
                    height_max_cm = 2.54 * height_max

                if depth_min:
                    depth_min_m = 0.0254 * depth_min
                    depth_min_i = depth_min
                    depth_min_cm = 2.54 * depth_min

                if depth_max:
                    depth_max_m = 0.0254 * depth_max
                    depth_max_i = depth_max
                    depth_max_cm = 2.54 * depth_max

        if(request.POST.get('category', None)):
            category = request.POST['category'].replace('[', '').replace(']', '').replace('"', '').strip().split(',')
            temp_element = []
            for element in category:
                if element != 'mixedMedia':
                    temp_element.append(element)
                else:
                    temp_element = temp_element + ['glass', 'ceramicPottery']

            category = temp_element


        if(request.POST.get('subcategory', None)):
            subcategory = request.POST['subcategory'].replace('[', '').replace(']', '').replace('"', '').strip().split(',')
            if 'other' in subcategory:
                subcategory += product_choices.sub_type_two.keys()

        if(request.POST.get('style', None)):
            style = request.POST['style'].replace('[', '').replace(']', '').replace('"', '').strip().split(',')

        if(request.POST.get('color', None)):
            color_list = request.POST['color'].replace('[', '').replace(']', '').replace('"', '').strip().split(',')
            
        if len(color_list) > 0:

            color_set = set()
            for i in color_list:
                if len(i) > 0:
                    color_set.update(product_choices.color[i]['group'])

            if len(color_set) > 0:
                color_list = list(color_set)

    
        # If no price option is choosen, then we should display all the prices.
        if request.POST.get('min_price', None) and len(request.POST.get('min_price', '')) > 0:
            if(request.POST['min_price'][-1] == 'l'):
                price_factor_above = False
            elif(request.POST['min_price'][-1] == 'g'):
                price_factor_above = True

            min_price = int(request.POST['min_price'][0:-1])

        category_id = list(Category.objects.filter(category_name__in = category).values_list('id', flat=True))
        subcategory_id = list(SubCategory.objects.filter(subcategory_name__in = subcategory).values_list('id', flat=True))
        style_id = list(Style.objects.filter(style_value__in = style).values_list('id', flat=True))


        products = Product.objects.filter(available=True)
        if len(category_id) > 0:
            products = products.filter(category_id__in=category_id, available=True)

        if len(subcategory_id) > 0:
            products = products.filter(subcategory_id__in=subcategory_id, available=True)

        if len(style_id) > 0:
            custom_query = functools.reduce(operator.or_, (Q(styles__icontains= str(item)) for item in style_id))
            products = Product.objects.filter(custom_query,  available=True)

        if len(color_list) > 0 and color_list[0] is not '':
            products = products.filter(Q(color__in=color_list) | Q(color_1__in=color_list) | Q(color_2__in=color_list) | Q(color_3__in=color_list) | Q(color_4__in=color_list)).filter(available=True)


        if measurement_unit:
            products = products.filter((Q(dim_measure= 'm') & (Q(width__gte= width_min_m)  & Q(width__lte= width_max_m) ) & (Q(height__gte= height_min_m)  & Q(height__lte= height_max_m) ) & ((Q(depth__gte= depth_min_m)  & Q(depth__lte= depth_max_m) ) | Q(depth__isnull= True))) | 

                (Q(dim_measure= 'cm')  & (Q(width__gte= width_min_cm)  & Q(width__lte= width_max_cm) ) & (Q(height__gte= height_min_cm)  & Q(height__lte = height_max_cm) ) & ((Q(depth__gte = depth_min_cm)  & Q(depth__lte = depth_max_cm)) | Q(depth__isnull = True)) ) |

                (Q(dim_measure= 'inches')  & (Q(width__gte= width_min_i)  & Q(width__lte= width_max_i) ) & (Q(height__gte= height_min_i)  & Q(height__lte= height_max_i) ) & ((Q(depth__gte= depth_min_i)  & Q(depth__lte= depth_max_i) ) | Q(depth__isnull= True) ) )).filter(available=True)

        if (not min_price_custom) and (not max_price_custom):

            if (min_price is not None) and (min_price > 0):
                if (price_factor_above):
                    
                    products = products.filter(price__gte=min_price).filter(available=True)
                else:
                    
                    products = products.filter(price__lte=min_price).filter(available=True)
        else:
            
            if (min_price_custom) and (max_price_custom):
                
                products = products.filter(Q(price__gte=abs(min_price_custom)) & Q(price__lte=abs(max_price_custom))).filter(available=True)

            elif (not min_price_custom) and (max_price_custom):

                products = products.filter(Q(price__lte=abs(max_price_custom))).filter(available=True)

            elif (min_price_custom) and (not max_price_custom):
                
                products = products.filter(Q(price__gte=abs(min_price_custom))).filter(available=True)

            elif (not min_price_custom) and (max_price_custom):
                
                products = products.filter(Q(price__lte=abs(max_price_custom))).filter(available=True)

        if request.POST.get('is_curator', 'false') == 'true':
            products = products.filter(curator_pick=True)

        if not sort_by:

            if products.count() > 0:
                products = products.order_by('-date')

        if sort_by == 'hf':
            
            products = products.order_by('-price')
        elif sort_by == 'lf':
            products = products.order_by('price')
            

        paginator = Paginator(products, 10)
        
        if not sort_by:

            np.random.seed(datetime.today().day)

            mapping_page_with_random = np.random.permutation(paginator.num_pages)
            mapping_page_with_random[np.where(mapping_page_with_random == 0)[0]] = paginator.num_pages
            page = list(mapping_page_with_random)[page-2]

        print(page)
        paged_art = paginator.page(page)


        current_product_count = len(paged_art)
        art_grouped_list = []
        user_wishlist = []
        user_authenticated = False

        if request.user.is_authenticated:
            user_authenticated = True
            user_wishlist = get_user_wish_list_products(UserInfo.objects.get(user=request.user))


        for j in range(0, current_product_count):
            temp_dict = {
                        'pk' : str(paged_art[j].id),
                        'authenticated' : user_authenticated,
                        'fields' : {
                            'art_title' : paged_art[j].art_title,
                            'height' : paged_art[j].height,
                            'depth' : paged_art[j].depth,
                            'width' : paged_art[j].width,
                            'price' : paged_art[j].price,
                            'image' : str(paged_art[j].image),
                            'sold' : paged_art[j].sold,
                            'available': paged_art[j].available,
                            'dim_measurement': paged_art[j].dim_measure,
                            'first_name' : paged_art[j].owner.user.first_name,
                            'last_name' : paged_art[j].owner.user.last_name,
                            'username' : paged_art[j].owner.user.username,
                            'img_host_url' : settings.BASE_AWS_IMG_URL,
                            'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
                        }
                    }
            if str(paged_art[j].id) in user_wishlist:
                temp_dict['fields']['fav'] = True
            else:
                temp_dict['fields']['fav'] = False

            art_grouped_list.append(temp_dict)
        if not sort_by:
            random.shuffle(art_grouped_list)
        return JsonResponse(art_grouped_list, safe=False)
    except Exception as e:
        logging.getLogger("error_logger").error('Error on line {}'.format(sys.exc_info()[-1].tb_lineno) + ' ' + type(e).__name__ + ' ' + str(e))
        return JsonResponse('[]', safe=False)


def show_search(request, type_, value):
    """ This method is used to display the search page.

        Args:
            request: The request object.

        Returns:
            It renders the arts.html page.
    """
    products = None
    # Below two are used to select in the filter option
    active_field = None
    active_value = None

    page = 1
    try:
        if type_.strip() == 'country':
            if value == 'shipcan':
                products = Product.objects.filter(show_shipping_price_can=True, available=True)
            elif value == 'shipus':
                products = Product.objects.filter(show_shipping_price_us=True, available=True)
            elif value == 'shipeurope':
                products = Product.objects.filter(show_shipping_price_europe=True, available=True)
            elif value == 'shipuk':
                products = Product.objects.filter(show_shipping_price_uk=True, available=True)
            elif value == 'shipasia':
                products = Product.objects.filter(show_shipping_price_asia=True, available=True)
            elif value == 'shipaunz':
                products = Product.objects.filter(show_shipping_price_aunz=True, available=True)


        if type_ == 'category':


            if value.strip() == "mixedMedia":
                category_id = list(Category.objects.filter(category_name__in = ['glass', 'ceramicPottery']).values_list('id', flat=True))
            else:
                category_id = list(Category.objects.filter(category_name__in = [value.strip(),]).values_list('id', flat=True))

            products = Product.objects.filter(category_id=category_id[0], available=True)
            active_value = value
            active_field = type_

        elif type_ == 'curator':
            products = Product.objects.filter(curator_pick=True, available=True)
            active_value = value
            active_field = type_

        elif type_ == 'price':
            code_and_price = value.strip().split('-')
            if code_and_price[0] == 'price_max':
                products = Product.objects.filter(price__lte=int(code_and_price[1]), available=True)
            elif code_and_price[0] == 'price_min':
                products = Product.objects.filter(price__gt=int(code_and_price[1]), available=True)
            elif code_and_price[0] == 'price_min_max':
                products = Product.objects.filter(price__gt=int(code_and_price[1]), price__lte=int(code_and_price[2]), available=True)
            active_value = value
            active_field = type_

        elif type_ == 'style':
            style_code = value.strip()
            style_obj = Style.objects.filter(style_value=style_code)
            products = Product.objects.filter(styles__icontains = style_obj[0].id,  available=True)
            active_value = style_code
            active_field = type_

        elif type_ == 'art' and value.strip() == 'all':
            products = Product.objects.filter(available=True)
            active_value = None
            active_field = None

        if products.count() > 0:
            products = products.order_by('-date')

        paginator = Paginator(products, 10)
        
        np.random.seed(datetime.today().day)
        mapping_page_with_random = np.random.permutation(paginator.num_pages)
        mapping_page_with_random[np.where(mapping_page_with_random == 0)[0]] = paginator.num_pages
        page = list(mapping_page_with_random)[page-2]

        paged_art = paginator.page(page)

        current_product_count = len(paged_art)
        art_grouped_list = []

        user_wishlist = []

        if request.user.is_authenticated:
            user_wishlist = get_user_wish_list_products(UserInfo.objects.get(user=request.user))

        for i in range(0, current_product_count, 2):
            temp = []
            for j in range(i, i+2):
                if j < current_product_count:

                    if str(paged_art[j].id) in user_wishlist:

                        temp.append({'art_obj' : paged_art[j], 'liked':True})
                    else:
                        temp.append({'art_obj' : paged_art[j], 'liked':False})
                else:
                    break

            art_grouped_list.append(temp)

        random.shuffle(art_grouped_list)
        context = {
                'category' : product_choices.category,
                # 'subcategory' : {**product_choices.sub_type_one, **product_choices.sub_type_two},
                'subcategory' : product_choices.grouped_sub_type,
                'style' : product_choices.styles,
                # 'products' : paged_art,
                'active_field' : active_field,
                'active_value' : active_value,
                'grouped_art' : art_grouped_list,
                'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
                'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
                'color' : product_choices.color,
            }

    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
        context = {
                'category' : product_choices.category,
                # 'subcategory' : {**product_choices.sub_type_one, **product_choices.sub_type_two},
                'subcategory' : product_choices.grouped_sub_type,
                'style' : product_choices.styles,
                'color' : product_choices.color,
                # 'products' : paged_art,
                'active_field' : active_field,
                'active_value' : active_value,
                'grouped_art' : None,
                'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
                'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
            }

    
    return render(request, 'products/arts.html', context)


@login_required
def get_user_wish_list(request):

    try:
        obj = WishlistProduct.objects.filter(user=UserInfo.objects.get(user=request.user)).order_by('-date')
        paginator = Paginator(obj, 10)

        page_number = int(request.GET.get('page', 1))
        if page_number > paginator.num_pages:
            page_number = 1

        paged_art = paginator.get_page(page_number)

    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
        paged_art = None

    return render(request, 'products/wishlist.html', {'arts' : paged_art, 'category' : product_choices.category, 'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL, 'img_optimize_param_large' : settings.IMG_OPTIMIZE_PARAM_LARGE})
    

def edit_art(request):
    """ This method is used to edit the existing art.

    Args:
        request: The request object.

    Returns:
        myart.html page
    """

    success = False

    message = None
    
    if request.user.is_authenticated:
        try:

            if request.method == 'POST':
                if request.POST.get('id'):

                    if Product.objects.get(id=request.POST['id']):

                        if request.POST['artname'] and \
                            request.POST['artdescription'] and \
                            request.POST['tags2'] and \
                            request.POST['height'] and \
                            request.POST['width'] and \
                            request.POST['price'] and \
                            request.POST['measure']:

                            title = request.POST['artname']
                            desc = request.POST['artdescription']
                            tags = request.POST['tags2']
                            style_list = request.POST.getlist('style_input')
                            height = 0
                            width = 0
                            depth = 0

                            measure = request.POST['measure']
                            styles = None



                            if(len(style_list) > 1):
                                # styles_str = request.POST.get('style_art_post_data_hidden', '').split(",")
                                styles = list(Style.objects.filter(style_value__in = style_list).values_list('id', flat=True))

                        
                            if measure not in product_choices.dim_measurement.values():
                                measure  = None
                                success = False
                                context = display(request)
                                message_context = {'success':success, 'fail':fail, 'message':'Invalid input data'}
                                return render(request, 'profile/my_art.html', {**context, **message_context})


                            try:
                                price = int(round(float(request.POST['price'])))
                                s_price_can = int(round(float(request.POST.get('shipcanada', 0)))) if int(round(float(request.POST.get('shipcanada', 0)))) > 0 else 0
                                s_price_us = int(round(float(request.POST.get('shipus', 0)))) if int(round(float(request.POST.get('shipus', 0)))) > 0 else 0
                                s_price_uk = int(round(float(request.POST.get('shipuk', 0)))) if int(round(float(request.POST.get('shipuk', 0)))) > 0 else 0
                                s_price_aunz = int(round(float(request.POST.get('shipaunz', 0)))) if  int(round(float(request.POST.get('shipaunz', 0)))) > 0 else 0
                                s_price_asia = int(round(float(request.POST.get('shipasia', 0)))) if int(round(float(request.POST.get('shipasia', 0)))) > 0 else 0
                                s_price_europe = int(round(float(request.POST.get('shipeurope', 0)))) if int(round(float(request.POST.get('shipeurope', 0)))) > 0 else 0
                                s_price_other = int(round(float(request.POST.get('shipother', 0)))) if int(round(float(request.POST.get('shipother', 0))))  > 0 else 0

                                if request.POST.get('depth'):
                                    if round(float(request.POST['depth']), 2) > 0:
                                        depth = round(float(request.POST['depth']), 2)

                                width = round(float(request.POST['width']), 2)
                                height = round(float(request.POST['height']), 2)

                            except ValueError as e:
                                context = display(request)
                                message_context = {'success': False, 'message':'Invalid input. Please try again'}
                                return render(request, 'profile/my_art.html', {**context, **message_context})

                            context = display(request)
                            product_data = Product.objects.get(id=request.POST['id'])
                            product_data.art_title = title
                            product_data.art_desc = desc
                            product_data.tags = tags

                            if height > 0:
                                product_data.height = height

                            if width > 0:
                                product_data.width = width

                            if depth > 0:
                                product_data.depth = depth

                            if price > 0:
                                product_data.price = price

                            if measure:
                                product_data.dim_measure = measure

                            product_data.shipping_price_can = s_price_can
                            product_data.shipping_price_us = s_price_us
                            product_data.shipping_price_uk = s_price_uk
                            product_data.shipping_price_aunz = s_price_aunz
                            product_data.shipping_price_asia = s_price_asia
                            product_data.shipping_price_europe = s_price_europe
                            product_data.shipping_price_other = s_price_other
                            product_data.styles = styles
                            product_data.save()
                            success = True
                            message = 'Changed successfully'

                else:

                    success = False
                    context = display(request)
                    message_context =  {'success':success, 'message':'No product information'}
                    return render(request, 'profile/my_art.html', {**context, **message_context})

        except Exception as e:
            logging.getLogger("error_logger").error(str(e))
            success = False
            context = display(request)
            message_context = {'success':success, 'message':'Something went wrong'}
            return render(request, 'profile/my_art.html', {**context, **message_context})

    else:
        return redirect('login')

    message_context = {'success':success, 'message': message}
    context = display(request)
    return render(request, 'profile/my_art.html', {**context, **message_context})



@login_required
def delete_art(request):
    """ This method is used to delete an art.

    Args:
        request: The request object.

    Returns:
        JSON Object"""
    if request.user.is_authenticated:
        try:
            if request.method == 'POST':
                if request.POST.get('id'):
                    if Product.objects.get(id=request.POST['id']):
                        product_data = Product.objects.get(id=request.POST['id'])
                        product_data.available = False
                        product_data.save()
                        response = {
                                    'status' : 'success',
                                    'message' : 'Art removed.',
                                }

                else:
                    response = {
                                    'status' : 'fail',
                                    'message' : 'No product information.',
                                }

        except Exception as e:

            response = {
                        'status' : 'fail',
                        'message' : 'Something went wrong.',
                    }

            logging.getLogger("error_logger").error(str(e))

    else:
        response = {
                    'status' : 'fail',
                    'message' : 'User not authenticated.',
                }

    return JsonResponse(response)




@login_required
def my_art(request):
    """ This method is display the art of a particular user.

    Args:
        request: The request object.

    Returns:
        It renders the my_art.html page.

    """

    context = display(request)
    context['style_id_mapping'] = Style.objects.all()
    context['material_id_mapping'] = Material.objects.all()
    return render(request, 'profile/my_art.html', context)




def add_art(request):
    """ This method is used to  upload an art.
    This method only takes POST request. Otherwise, it will the error message.


    Args:
        request: The request object.

    Returns:
        JSON object
    """

    if request.user.is_authenticated:
        try :
            if request.method == 'POST':
                with transaction.atomic():
                    json_data = json.loads(request.body)

                    if json_data['art_img'] and \
                            (json_data['color'] or \
                                json_data['color_1'] or \
                                json_data['color_2'] or \
                                json_data['color_3'] or \
                                json_data['color_4']) and \
                            json_data['title'] and \
                            json_data['desc'] and \
                            json_data['height'] and \
                            json_data['width'] and \
                            json_data['cat'] and \
                            json_data['subcat'] and \
                            json_data['price'] and \
                            json_data['measure']:

                        img = json_data['art_img']
                        title = json_data['title'].strip()
                        color = json_data['color']
                        color_1 = json_data['color_1']
                        color_2 = json_data['color_2']
                        color_3 = json_data['color_3']
                        color_4 = json_data['color_4']
                        desc = json_data['desc'].strip()
                        measure = json_data['measure']
                        category = json_data['cat']
                        subcategory = json_data['subcat']
                        tags = ''


                        if len(json_data['tags']) > 0:
                            # tags = [i + ',' for i in json_data['tags']][0][:-1]
                            for i in json_data['tags']:
                                tags = tags + i + ','
                            tags = tags[0:len(tags)-1]
                        


                        price = None
                        styles = None
                        materials = None
                        is_signed = None
                        is_framed = None



                        if(len(json_data['styles']) > 0):
                            styles_str = json_data['styles']
                            styles = list(Style.objects.filter(style_value__in = styles_str).values_list('id', flat=True))
                        else:
                            response = {
                                'status' : 'fail',
                                'message' : 'Please select the styles',
                                }

                            return JsonResponse(response, status=500)



                        if(len(json_data['materials']) > 0):
                            materials_str = json_data['materials']
                            materials = list(Material.objects.filter(material_value__in = materials_str).values_list('id', flat=True))
                        else:
                            response = {
                                    'status' : 'fail',
                                    'message' : 'Please select the materials',
                                    }
                            return JsonResponse(response, status=500)



                        if(json_data['is_signed'].lower() == 'yes'):
                            is_signed = True
                        elif (json_data['is_signed'].lower() == 'no'):
                            is_signed = False
                        else:
                            response = {
                                    'status' : 'fail',
                                    'message' : 'Please select an option for signed',
                                    }
                            return JsonResponse(response, status=500)


                        if(json_data['is_framed_ready'].lower() == 'yes'):
                            is_framed = 'yes'
                        elif(json_data['is_framed_ready'].lower() == 'no'):
                            is_framed = 'no'
                        elif(json_data['is_framed_ready'].lower() == 'other'):
                            is_framed = 'other'
                        else:
                            response = {
                                    'status' : 'fail',
                                    'message' : 'Please select an option for framed and ready to hang.',
                                    }
                            return JsonResponse(response, status=500)


                        try:

                            if json_data['height'] is None:
                                response = {
                                'status' : 'fail',
                                'message' : 'Please enter the height',
                                }
                                return JsonResponse(response, status=500)
                            else:
                                height = round(float(json_data['height']), 2)


                            if json_data['width'] is None:
                                response = {
                                'status' : 'fail',
                                'message' : 'Please enter the width',
                                }
                                return JsonResponse(response, status=500)
                            else:
                                width = round(float(json_data['width']), 2)


                            if json_data['depth']:
                                depth = round(float(json_data['depth']), 2)
                            else:
                                depth = None

                            if (json_data['price'] is None):
                                response = {
                                'status' : 'fail',
                                'message' : 'Please enter a price',
                                }
                                return JsonResponse(response, status=500)
                            else:
                                price = int(round(float(json_data['price'])))


                            if (json_data['s_price_can'] is None) :
                                s_price_can = 0
                            else:
                                s_price_can = int(round(float(json_data['s_price_can'])))


                            if (json_data['s_price_us'] is None) :
                                s_price_us = 0
                            else:
                                s_price_us = int(round(float(json_data['s_price_us'])))


                            if (json_data['s_price_uk'] is None):
                                s_price_uk = 0
                            else:
                                s_price_uk = int(round(float(json_data['s_price_uk'])))

                            if (json_data['s_price_aunz'] is None):
                                s_price_aunz = 0
                            else:
                                s_price_aunz = int(round(float(json_data['s_price_aunz'])))

                            if (json_data['s_price_asia'] is None):
                                s_price_asia = 0
                            else:
                                s_price_asia = int(round(float(json_data['s_price_asia'])))

                            if (json_data['s_price_europe'] is None):
                                s_price_europe = 0
                            else:
                                s_price_europe = int(round(float(json_data['s_price_europe'])))


                            if (json_data['s_price_other'] is None):
                                s_price_other = 0
                            else:
                                s_price_other = int(round(float(json_data['s_price_other'])))

                        except ValueError as e:
                            raise InvalidFormatException('Price and shipping should be numbers.')


                        if measure not in product_choices.dim_measurement.values():
                            raise InvalidFormatException('Invalid input data.')

                        if not (float(height) >= 0 and \
                                float(width) >= 0 and \
                                float(price) >= 0):
                            raise InvalidFormatException('Cannot input negative numbers.')



                        show_price_can = json_data['show_price_can']
                        show_price_us = json_data['show_price_us']
                        show_price_uk = json_data['show_price_uk']
                        show_price_aunz = json_data['show_price_aunz']
                        show_price_asia = json_data['show_price_asia']
                        show_price_europe = json_data['show_price_europe']
                        show_price_other = json_data['show_price_other']

                        if not (show_price_can or show_price_us or show_price_uk or
                            show_price_aunz or show_price_asia or
                            show_price_europe or show_price_other):
                            response = {
                                'status' : 'fail',
                                'message' : 'Please enter at least one shipping price',
                                }
                            return JsonResponse(response, status=500)

                        category_obj = Category.objects.get(category_name=category)
                        subcategory_obj = SubCategory.objects.get(subcategory_name=subcategory)

                        additional_img_1 = None
                        additional_img_2 = None
                        additional_img_3 = None
                        additional_img_4 = None


                        if json_data['additional_img_1'] is not None:
                            additional_img_1 = decode_base64_file(json_data['additional_img_1'], '1')

                        if json_data['additional_img_2'] is not None:
                            additional_img_2 = decode_base64_file(json_data['additional_img_2'], '2')

                        if json_data['additional_img_3'] is not None:
                            additional_img_3 = decode_base64_file(json_data['additional_img_3'], '3')

                        if json_data['additional_img_4'] is not None:
                            additional_img_4 = decode_base64_file(json_data['additional_img_4'], '4')



                        user_info = UserInfo.objects.get(user = request.user)
                        new_product = Product(
                                        art_title=title,
                                        art_desc = desc,
                                        tags=tags,
                                        height=height,
                                        width=width,
                                        depth=depth,
                                        category=category_obj,
                                        subcategory=subcategory_obj,
                                        price=price,
                                        shipping_price_can=s_price_can,
                                        shipping_price_us=s_price_us,
                                        shipping_price_aunz=s_price_aunz,
                                        shipping_price_uk=s_price_uk,
                                        shipping_price_asia=s_price_asia,
                                        shipping_price_europe=s_price_europe,
                                        shipping_price_other=s_price_other,
                                        owner=user_info,
                                        image=decode_base64_file(img),
                                        color=color,
                                        color_1=color_1,
                                        color_2=color_2,
                                        color_3=color_3,
                                        color_4=color_4,
                                        additional_image_1=additional_img_1,
                                        additional_image_2=additional_img_2,
                                        additional_image_3=additional_img_3,
                                        additional_image_4=additional_img_4,
                                        dim_measure=measure,
                                        show_shipping_price_us = True if show_price_us==True else False,
                                        show_shipping_price_can = True if show_price_can==True else False,
                                        show_shipping_price_uk = True if show_price_uk==True else False,
                                        show_shipping_price_aunz = True if show_price_aunz==True else False,
                                        show_shipping_price_asia = True if show_price_asia==True else False,
                                        show_shipping_price_europe = True if show_price_europe==True else False,
                                        show_shipping_price_other = True if show_price_other==True else False,
                                        is_signed = is_signed,
                                        is_framed_or_hang = is_framed,
                                        styles = styles,
                                        materials = materials
                                        )

                        new_product.save()

                        response = {
                            'status' : 'success',
                            'message' : 'Art uploaded.',
                            'product_id': new_product.id
                            }

                    else:
                        raise PostDataMissingException('Missing few input fields.')

            else :
                raise NotPostRequestException('Invalid request type.')

        except (NotPostRequestException, InvalidFormatException, PostDataMissingException) as e:

            response = {
                        'status' : 'fail',
                        'message' : str(e),
                    }


        except Exception as e:

            response = {
                        'status' : 'fail',
                        'message' : 'There was an error uploading your art. Please contact info@thebidgala.co',
                    }


            logging.getLogger("error_logger").error(str(e))

    else:
        response = {
                    'status' : 'login',
                    'message' : 'Please login to upload',
                }

    return JsonResponse(response)




def product_view(request, id):
    """ This method is used to render the product_view page.

    Args:
        request: The request object.

    Returns:
        It renders the product_view.html page.

    """
    context = None
    try:
        product_obj = Product.objects.filter(id=id.strip()).filter(available=True)

        if product_obj.count() == 1:
            user_actual_id = product_obj[0].owner.id
            user_first_name = product_obj[0].owner.user.first_name
            user_last_name = product_obj[0].owner.user.last_name
            art_title = product_obj[0].art_title
            category_type = Category.objects.get(id=product_obj[0].category_id).category_val
            subcategory_type = SubCategory.objects.get(id=product_obj[0].subcategory_id).subcategory_val

            owner_stripe_account = Stripe.objects.filter(user=user_actual_id)

            product_owner_user_info = UserInfo.objects.get(id=user_actual_id)

            more_products = Product.objects.filter(owner=product_owner_user_info, available=True, sold=False).exclude(id=id.strip()).order_by('-date')[:6]       

            product = product_obj.values('id', 'price', 'art_desc', 'height', 'width', 'depth', 'dim_measure', 'image', 'additional_image_1', 'additional_image_4', 'additional_image_2', 'additional_image_3', 'curator_pick', 'available', 'sold', 'comment_count')
            list_additional_img = []
            show_shipping_prices = {}
            stripe_shipping_data = {}

            if(product_obj[0].additional_image_1):
                list_additional_img.append(product_obj[0].additional_image_1)

            if product_obj[0].additional_image_2:
                list_additional_img.append(product_obj[0].additional_image_2)

            if product_obj[0].additional_image_3:
                list_additional_img.append(product_obj[0].additional_image_3)

            if product_obj[0].additional_image_4:
                list_additional_img.append(product_obj[0].additional_image_4)

            if(product_obj[0].show_shipping_price_us and product_obj[0].shipping_price_us >= 0):
                show_shipping_prices['US'] = product_obj[0].shipping_price_us
                stripe_shipping_data['US'] = {'countries':choices.stripe_shipping_support['US'], 'price':product_obj[0].shipping_price_us}

            if(product_obj[0].show_shipping_price_can and product_obj[0].shipping_price_can >= 0):
                show_shipping_prices['CANADA'] = product_obj[0].shipping_price_can
                stripe_shipping_data['CANADA'] = {'countries':choices.stripe_shipping_support['CANADA'], 'price':product_obj[0].shipping_price_can}

            if(product_obj[0].show_shipping_price_uk and product_obj[0].shipping_price_uk >= 0):
                show_shipping_prices['UK'] = product_obj[0].shipping_price_uk
                stripe_shipping_data['UK'] = {'countries':choices.stripe_shipping_support['UK'], 'price':product_obj[0].shipping_price_uk}


            if(product_obj[0].show_shipping_price_asia and product_obj[0].shipping_price_asia >= 0):
                show_shipping_prices['ASIA'] = product_obj[0].shipping_price_asia
                stripe_shipping_data['ASIA'] = {'countries':choices.stripe_shipping_support['ASIA'], 'price':product_obj[0].shipping_price_asia}

            if(product_obj[0].show_shipping_price_aunz and product_obj[0].shipping_price_aunz >= 0):
                show_shipping_prices['AUSTRALIA/NEW ZEALAND'] = product_obj[0].shipping_price_aunz
                stripe_shipping_data['AUSTRALIA'] = {'countries':choices.stripe_shipping_support['AUSTRALIA'], 'price':product_obj[0].shipping_price_aunz}
                stripe_shipping_data['NEW ZEALAND'] = {'countries':choices.stripe_shipping_support['NEW ZEALAND'], 'price':product_obj[0].shipping_price_aunz}

            if(product_obj[0].show_shipping_price_europe and product_obj[0].shipping_price_europe >= 0):
                show_shipping_prices['EUROPE'] = product_obj[0].shipping_price_europe
                stripe_shipping_data['EUROPE'] = {'countries':choices.stripe_shipping_support['EUROPE'], 'price':product_obj[0].shipping_price_europe}

            if(product_obj[0].show_shipping_price_other and product_obj[0].shipping_price_other >= 0):
                show_shipping_prices['OTHER'] = product_obj[0].shipping_price_other
                stripe_shipping_data['OTHER'] = {'countries':choices.stripe_shipping_support['OTHER'], 'price':product_obj[0].shipping_price_other}

            professional_verified = False
            customer = None
            customer_payment_methods = None
            is_fav = False
            if request.user.is_authenticated:
                current_user = UserInfo.objects.get(user=request.user)
                is_fav = is_user_wish_list_product(current_user, product_obj[0])

                if current_user.stripe_customer_id:
                    [customer, payment_methods] = get_stripe_customer(current_user)
                    customer_payment_methods = payment_methods.data

                professional_verified = True if (current_user.is_professional and current_user.company_email_verified) else False

            if professional_verified:
                professional_discount_price = round(product_obj[0].price - round(product_obj[0].price * constants.PROFESSIONAL_DISCOUNT, 2), 2)
            else:
                professional_discount_price = product_obj[0].price

            comments = Comment.objects.filter(product_id=product_obj[0].id, show=True).order_by("-created_date")

            context = {
                'product':product[0],
                'first_name':user_first_name,
                'last_name':user_last_name,
                'art_title':art_title,
                'category_type' : category_type,
                'subcategory_type' : subcategory_type,
                'user_actual_id' : user_actual_id,
                'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
                'additional_img' : list_additional_img,
                'show_shipping_prices' : show_shipping_prices,
                'category' : product_choices.category,
                'bidgala_publish_key' : settings.STRIPE_PUBLISHABLE_KEY,
                'owner_stripe_account_id': owner_stripe_account[0].stripe_account_id if owner_stripe_account.count() > 0 else None,
                'logged_in_user_id': request.user,
                'product_owner_user': product_owner_user_info.user,
                'is_product_owner': True if product_owner_user_info.user == request.user else False,
                'professional_verified' : professional_verified,
                'professional_discount_price' : professional_discount_price,
                'stripe_shipping_support': stripe_shipping_data,
                'customer': customer,
                'customer_payment_methods': customer_payment_methods,
                'comments': comments,
                'is_fav' : is_fav,
                'more_products': more_products,
                'img_optimize_param_large':settings.IMG_OPTIMIZE_PARAM_LARGE,
                }

    except InvalidFormatException as e:
        context = {'product':None}
        logging.getLogger("error_logger").error(str(e))

    return render(request, 'products/product_view.html', context)



def get_search_results(request):
    """ This method is used to provide search functionality

    Search is based on the following citerion:
    art_title
    art_desc
    tags
    category_id
    subcategory
    styles
    materials

    Args:
        request: The request object.

    Returns:
        It renders art.html page

    """
    min_per_page = 20

    context = {
            'category' : product_choices.category,
            # 'subcategory' : {**product_choices.sub_type_one, **product_choices.sub_type_two},
            'subcategory' : product_choices.grouped_sub_type,
            'style' : product_choices.styles,
            'BASE_AWS_IMG_URL' : settings.BASE_AWS_IMG_URL,
            'img_optimize_param' : settings.IMG_OPTIMIZE_PARAM,
            'color' : product_choices.color,
        }
    try:
        if request.method == 'POST':
            keyword = request.POST.get('keyword', '').strip()

            vector = SearchVector('owner__user__last_name', weight='A') + SearchVector('owner__user__first_name', weight='A') + SearchVector('owner__user__username', weight='A') + SearchVector('category__category_name', weight='B') + SearchVector('subcategory__subcategory_name', weight='B') + SearchVector('tags', weight='C') + SearchVector('materials', weight='C') + SearchVector('styles', weight='D')  + SearchVector('art_title', weight='B') + SearchVector('art_desc', weight='C')
            query = SearchQuery(keyword)
            rank = SearchRank(vector, query, weights=[0.5, 0.6, 0.7, 1])
            relevant = Product.objects.annotate(rank=rank).filter(available=True).filter(rank__gte=0.4).order_by('-rank')

            max_count = min(relevant.count(), min_per_page)
            paginator = Paginator(relevant, max_count)
            paged_art = paginator.page(1)
            current_product_count = relevant.count()
            art_grouped_list = []
            user_wishlist = []
            if request.user.is_authenticated:
                user_wishlist = get_user_wish_list_products(UserInfo.objects.get(user=request.user))


            for i in range(0, current_product_count, 2):
                temp = []
                for j in range(i, i+2):
                    if j < min_per_page and j < len(paged_art):
                        if str(paged_art[j].id) in user_wishlist:
                            temp.append({'art_obj' : paged_art[j], 'liked':True})
                        else:
                            temp.append({'art_obj' : paged_art[j], 'liked':False})
                    else:
                        break
                if len(temp) > 0:
                    art_grouped_list.append(temp)

            # random.shuffle(art_grouped_list)
            context['grouped_art'] = art_grouped_list

    except Exception as e:
        logging.getLogger("error_logger").error('Error on line {}'.format(sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

    return render(request, 'products/arts.html', context)



def set_favourite_product(request):
    """ This method is used to set the wishlist item
    for the login user.

    Args:
        request: The request object.

    Returns:
        It returns a json response

    """

    try:
        if request.user.is_authenticated:
            product_id = request.POST['id']
            user_info = UserInfo.objects.filter(user=request.user)
            product_obj = Product.objects.filter(id=product_id).filter(available=True)

            if user_info.count() < 1:
                return JsonResponse({'status':'User not found. Please login'}, status=200)

            if product_obj.count() < 1:
                return JsonResponse({'status':'Product not found'}, status=200)

            check_if_exists = WishlistProduct.objects.filter(user=user_info[0]).filter(product=product_obj[0])

            if check_if_exists.count() == 0:
                obj = WishlistProduct(user=user_info[0], product=product_obj[0])
                obj.save()

                return JsonResponse({'status':'added'}, status=200)
            else:
                check_if_exists.delete()
                return JsonResponse({'status':'removed'}, status=200)

        else:
            return JsonResponse({'status':'Authentication failed'}, status=200)
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
        return JsonResponse({'status':'fail'}, status=500)





# def art_upload_page(request):
# 	""" This method is redirect to the art upload page.

# 	Args:
# 		request: The request object.

# 	Returns:
# 		It renders the art_upload.html page.

# 	"""

# 	# If user is already logged in, then redirect to index.html
# 	if request.user.is_authenticated:

# 		show_page = False
# 		user = UserInfo.objects.get(user = request.user)

# 		content = {
# 			'category' : product_choices.category,
# 			'category_sell' : product_choices.category_sell,
# 			'dim_measurement' : product_choices.dim_measurement,
# 			'style' : product_choices.styles,
# 			'material' : product_choices.material,
# 		}

# 		return render(request, 'products/art_upload.html', content)

# 	messages = None
# 	messages.error(request, 'Please login to access the sell page.')
# 	return redirect('login')


def art_upload_page(request):
    """ This method is redirect to the art upload page.

    Args:
        request: The request object.

    Returns:
        It renders the art_upload.html page.

    """

    # If user is already logged in, then redirect to index.html


    show_page = False

    content = {
        'category' : product_choices.category,
        'category_sell' : product_choices.category_sell,
        'dim_measurement' : product_choices.dim_measurement,
        'style' : product_choices.styles,
        'material' : product_choices.material,
    }
    return render(request, 'products/art_upload.html', content)





@login_required
def add_comment(request):
    """ This method is used to create a comment for a product

    Args:
        request: The request object

    Returns:
        It return a json response with status code
    """
    try:
        with transaction.atomic():
            if request.method == 'POST':
                product_id = request.POST['product_id'].strip()
                comment = request.POST['comment'].strip()

                if len(comment) > 0:
                    user = UserInfo.objects.get(user=request.user)
                    BASE_IMG_URL = settings.BASE_AWS_IMG_URL
                    product_obj = Product.objects.get(id=product_id)
                    product_obj.comment_count+=1
                    product_obj.save()
                    comment_obj = Comment(body=comment, user=user, product_id=product_obj)
                    comment_obj.save()

                    if user.profile_img:
                        profile_img = BASE_IMG_URL + str(user.profile_img)
                    else:
                        profile_img = static('img/profile-icon.png')
                    try:
                        # if request.user != product_obj.owner.user:
                        if True:
                            from_email = settings.FROM_EMAIL
                            to_email = product_obj.owner.user.email
                            if len(product_obj.art_title) > 0:
                                subject='New comment on ' + product_obj.art_title
                            else:
                                subject='New comment on your art'


                            commented_by_name = request.user.first_name + ' ' + request.user.last_name
                            link_to_art = settings.HOST_BASE_URL + 'art/product_view/' + str(product_obj.id)

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
                            message_ = create_message(to_email, subject, email_template.receiveComment(product_obj.art_title if len(product_obj.art_title) > 0 else "your art", link_to_art, comment, commented_by_name))

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
                    except Exception as e:
                        logging.getLogger("error_logger").error(str(e))

                    data = [comment_obj.body, request.user.username, comment_obj.created_date, profile_img, comment_obj.id, product_obj.id]

                    return JsonResponse({'status':'success', 'data' : data}, status=200)
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
        messages.error(request, 'Comment could not be added.')
        return JsonResponse({'status':'fail'}, status=500)

@login_required
def delete_comment(request, product_id, comment_id):
    try:
        with transaction.atomic():
            user = UserInfo.objects.get(user=request.user)
            comment = Comment.objects.filter(id=comment_id)[0]
            if user == comment.user:
                comment.show = False
                comment.save()
                comment.product_id.comment_count = comment.product_id.comment_count - 1
                comment.product_id.save()

    except Exception as e:
        messages.error(request, 'Comment could not be deleted.')
        logging.getLogger("error_logger").error(str(e))


    return redirect('product_view', id=product_id)
