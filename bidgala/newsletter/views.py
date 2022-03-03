import email
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.http import JsonResponse

from .models import NewsletterUser
from accounts import choices
from products import choices as product_choices
from accounts.models import UserInfo, TermsAndConditions
from products.models import Product
from discover.models import Article
from pages.models import HomePage
from pages.utils import get_featured_artist, get_category, get_channel
from products import choices as product_choices


def NewsLetter(request):
    if request.method == 'POST':
        email_input = request.POST.get('email_value')
        new = NewsletterUser(email=email_input)
        new.save()
        
        products = Product.objects.filter(curator_pick=True, sold=False, available=True).order_by('-date')[0:10]
        # .distinct('Owner__id) causing items to shrink. So removed it.
        new_products = Product.objects.filter(sold=False, available=True).order_by('-date').order_by('owner__id')[0:10]
        discover_articles = Article.objects.filter(show=True).order_by('-created_date')[0:10]

        all_art_img = HomePage.objects.filter(value='shop_all_art')[0]
        advisory_img = HomePage.objects.filter(value='advisory')[0]

        channel_obj = get_channel()
        featured_artist = get_featured_artist()

        featured_artist_art = []

        product_featured_artist = []

        for i in featured_artist:
            data_temp = Product.objects.filter(owner=i).order_by('-date')[0:3]

            if data_temp.count() >= 1:
                product_featured_artist.append(data_temp[0:3])

        for i in featured_artist:
            temp_data = Product.objects.filter(owner=i).order_by('-date')

            if temp_data.count() >= 1:
                featured_artist_art.append(temp_data[0])

            # try:
            # 	featured_artist_products = Product.objects.filter(owner=i, available=True).order_by('-date')

            # except Product.DoesNotExist:
            # 	featured_artist_products = None

        category_obj = get_category()
        context = {
            'all_art_img': all_art_img.image,
            'advisory_img': advisory_img.image,
            'discover_articles': discover_articles,
            'category': product_choices.category,
            'subcategory': product_choices.subcategory,
            'products': products,
            'channels': channel_obj,
            'featured_artists': featured_artist_art,
            # 'featured_artist_products': featured_artist_products,
            'new_products': new_products,
            'category_objs': category_obj,
            'BASE_IMG_URL': settings.BASE_AWS_IMG_URL,
            'img_optimize_param': settings.IMG_OPTIMIZE_PARAM,
            'product_featured_artist': product_featured_artist,
        }

                
    return render(request,"pages/index.html", context)