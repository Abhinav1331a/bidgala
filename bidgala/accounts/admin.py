# Standard library imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse
from django.urls import path
from datetime import datetime, timedelta
from django.db.models import Sum
import operator
from functools import reduce 

# Related third party imports

# Local application/library specific imports
from .models import *
from chat.models import Message
from community.models import Post
import payments
import products


class StripeInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Stripe and Product Info'
        # app_label = 'accounts'


@staff_member_required
def my_custom_view(request):
	stripe_obj = payments.models.Stripe.objects.values('user')
	product_obj = products.models.Product.objects.values('owner').distinct()
	users_with_products = UserInfo.objects.filter(Q(id__in=product_obj))
	users = users_with_products.filter(~Q(id__in=stripe_obj))
	return render(request, 'custom_admin/unregistered_stripe.html', {'users':users})


class StripeInfoAdmin(admin.ModelAdmin):
    model = StripeInfo

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('custom/', my_custom_view, name=view_name),
        ]



class BioSearch(models.Model):
    class Meta:
        verbose_name_plural = 'User Bio Keyword search'


@staff_member_required
def biosearch_custom_view(request):
    context = {}
    if request.method == 'POST':
        keywords = request.POST.get('keywords', None)
        if keywords:
            keywords = keywords.split(',')
            query = reduce(operator.and_, (Q(bio__icontains = item) for item in keywords))
            obj = UserInfo.objects.filter(query)
            context = {'data' : obj}
        
    return render(request, 'custom_admin/bio_search.html', context)
        


class BioSearchAdmin(admin.ModelAdmin):
    model = BioSearch
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('custom/', biosearch_custom_view, name=view_name),
        ]





class UserSearch(models.Model):
    class Meta:
        verbose_name_plural = 'User info Keyword search'


@staff_member_required
def usersearch_custom_view(request):
    context = {}
    if request.method == 'POST':
       
        keywords = request.POST.get('keywords', None)
        if keywords:
            keywords = keywords.split(',')
           
            query = reduce(operator.and_, ((Q(user__first_name__icontains = item) | Q(user__last_name__icontains = item) | Q(user__username__icontains = item)) for item in keywords))
            obj = UserInfo.objects.filter(query)
          
            context = {'data' : obj}
        
    return render(request, 'custom_admin/user_search.html', context)
        


class UserSearchAdmin(admin.ModelAdmin):
    model = UserSearch
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('custom/', usersearch_custom_view, name=view_name),
        ]








class ArticleEdit(models.Model):
    class Meta:
        verbose_name_plural = 'Create and edit articles'

@staff_member_required
def article_custom_view(request):
    return render(request, 'custom_admin/article.html')


class ArticleAdmin(admin.ModelAdmin):
    model = ArticleEdit
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('custom/', article_custom_view, name=view_name),
        ]



class Stats(models.Model):
    class Meta:
        verbose_name_plural = 'Bidgala Stats'



@staff_member_required
def stats_custom_view(request):
    current_time = datetime.now(tz=timezone.utc)
    users = User.objects.all()
    user_info = UserInfo.objects.all()
    order_hold = payments.models.OrderHold.objects.all()
    order = payments.models.Orders.objects.filter(purchased=True)
    message = Message.objects.all()
    post = Post.objects.all()

    post_past_all = post.count()
    post_past_7 = post.filter(created_date__gte = current_time-timedelta(days=7)).count()
    post_past_30 = post.filter(created_date__gte = current_time-timedelta(days=30)).count()
    post_past_90 = post.filter(created_date__gte = current_time-timedelta(days=90)).count()

    order_hold_past_all = order_hold.filter(accepted=False, declined=False).count()
    order_hold_past_all_total = order_hold.filter(accepted=False, declined=False).aggregate(Sum('amount_total'))
    temp = order_hold.filter(accepted=False, declined=False).filter(created_timestamp__gte = current_time-timedelta(days=7))
    order_hold_past_7 = temp.count()
    order_hold_past_7_total = temp.aggregate(Sum('amount_total'))

    temp = order_hold.filter(accepted=False, declined=False).filter(created_timestamp__gte = current_time-timedelta(days=30))
    order_hold_past_30 = temp.count()
    order_hold_past_30_total = temp.aggregate(Sum('amount_total'))

    temp = order_hold.filter(accepted=False, declined=False).filter(created_timestamp__gte = current_time-timedelta(days=90))
    order_hold_past_90 = temp.count()
    order_hold_past_90_total = temp.aggregate(Sum('amount_total'))


    accepted_past_all = order_hold.filter(accepted=True, declined=False).count()
    accepted_past_all_total = order_hold.filter(accepted=True, declined=False).aggregate(Sum('amount_total'))
    temp = order_hold.filter(accepted=True, declined=False).filter(created_timestamp__gte = current_time-timedelta(days=7))
    accepted_past_7 = temp.count()
    accepted_past_7_total = temp.aggregate(Sum('amount_total'))

    temp = order_hold.filter(accepted=True, declined=False).filter(created_timestamp__gte = current_time-timedelta(days=30))
    accepted_past_30 = temp.count()
    accepted_past_30_total = temp.aggregate(Sum('amount_total'))

    temp = order_hold.filter(accepted=True, declined=False).filter(created_timestamp__gte = current_time-timedelta(days=90))
    accepted_past_90 = temp.count()
    accepted_past_90_total = temp.aggregate(Sum('amount_total'))


    tracking_provided_past_all = order.count()
    tracking_provided_past_all_total = order.aggregate(Sum('price'))
    
    temp = order.filter(order_date__gte = current_time-timedelta(days=7))
    tracking_provided_past_7 = temp.count()
    tracking_provided_past_7_total = temp.aggregate(Sum('price'))

    temp = order.filter(order_date__gte = current_time-timedelta(days=30))
    tracking_provided_past_30 = temp.count()
    tracking_provided_past_30_total = temp.aggregate(Sum('price'))

    temp = order.filter(order_date__gte = current_time-timedelta(days=90))
    tracking_provided_past_90 = temp.count()
    tracking_provided_past_90_total = temp.aggregate(Sum('price'))

    users_past_all = users.count()
    users_past_7 = users.filter(date_joined__gte = current_time-timedelta(days=7)).count()
    users_past_30 = users.filter(date_joined__gte = current_time-timedelta(days=30)).count()
    users_past_90 = users.filter(date_joined__gte = current_time-timedelta(days=90)).count()

    artist_past_all = user_info.filter(is_seller=True, is_buyer=False).count()
    artist_past_7 = user_info.filter(is_seller=True, is_buyer=False).filter(user__date_joined__gte = current_time-timedelta(days=7)).count()
    artist_past_30 = user_info.filter(is_seller=True, is_buyer=False).filter(user__date_joined__gte = current_time-timedelta(days=30)).count()
    artist_past_90 = user_info.filter(is_seller=True, is_buyer=False).filter(user__date_joined__gte = current_time-timedelta(days=90)).count()

    buyer_past_all = user_info.filter(is_seller=False, is_buyer=True).count()
    buyer_past_7 = user_info.filter(is_seller=False, is_buyer=True).filter(user__date_joined__gte = current_time-timedelta(days=7)).count()
    buyer_past_30 = user_info.filter(is_seller=False, is_buyer=True).filter(user__date_joined__gte = current_time-timedelta(days=30)).count()
    buyer_past_90 = user_info.filter(is_seller=False, is_buyer=True).filter(user__date_joined__gte = current_time-timedelta(days=90)).count()

    both_past_all = user_info.filter(is_seller=True, is_buyer=True).count()
    both_past_7 = user_info.filter(is_seller=True, is_buyer=True).filter(user__date_joined__gte = current_time-timedelta(days=7)).count()
    both_past_30 = user_info.filter(is_seller=True, is_buyer=True).filter(user__date_joined__gte = current_time-timedelta(days=30)).count()
    both_past_90 = user_info.filter(is_seller=True, is_buyer=True).filter(user__date_joined__gte = current_time-timedelta(days=90)).count()

    pro_past_all = user_info.filter(is_professional=True).count()
    pro_past_7 = user_info.filter(is_professional=True).filter(user__date_joined__gte = current_time-timedelta(days=7)).count()
    pro_past_30 = user_info.filter(is_professional=True).filter(user__date_joined__gte = current_time-timedelta(days=30)).count()
    pro_past_90 = user_info.filter(is_professional=True).filter(user__date_joined__gte = current_time-timedelta(days=90)).count()
    
    message_past_all = message.count()
    message_past_7 = message.filter(timestamp__gte = current_time-timedelta(days=7)).count()
    message_past_30 = message.filter(timestamp__gte = current_time-timedelta(days=30)).count()
    message_past_90 = message.filter(timestamp__gte = current_time-timedelta(days=90)).count()   

    artist_message_all = message.filter(origin_user__is_seller=True).count()
    artist_message_7 = message.filter(origin_user__is_seller=True).filter(timestamp__gte = current_time-timedelta(days=7)).count()
    artist_message_30 = message.filter(origin_user__is_seller=True).filter(timestamp__gte = current_time-timedelta(days=30)).count()
    artist_message_90 = message.filter(origin_user__is_seller=True).filter(timestamp__gte = current_time-timedelta(days=90)).count()

    buyer_message_all = message.filter(origin_user__is_buyer=True).count()
    buyer_message_7 = message.filter(origin_user__is_buyer=True).filter(timestamp__gte = current_time-timedelta(days=7)).count()
    buyer_message_30 = message.filter(origin_user__is_buyer=True).filter(timestamp__gte = current_time-timedelta(days=30)).count()
    buyer_message_90 = message.filter(origin_user__is_buyer=True).filter(timestamp__gte = current_time-timedelta(days=90)).count()

    total_visit_7  = user_info.filter(user_id__last_login__gte = current_time-timedelta(days=7)).count()
    total_visit_30 = user_info.filter(user_id__last_login__gte = current_time-timedelta(days=30)).count()
    total_visit_90 = user_info.filter(user_id__last_login__gte = current_time-timedelta(days=90)).count()

    artist_visit_7  =  user_info.filter(is_seller=True, is_buyer=False).filter(user_id__last_login__gte = current_time-timedelta(days=7)).count()
    artist_visit_30 =  user_info.filter(is_seller=True, is_buyer=False).filter(user_id__last_login__gte = current_time-timedelta(days=30)).count()
    artist_visit_90 =  user_info.filter(is_seller=True, is_buyer=False).filter(user_id__last_login__gte = current_time-timedelta(days=90)).count()

    buyer_visit_7  =  user_info.filter(is_seller=False, is_buyer=True).filter(user_id__last_login__gte = current_time-timedelta(days=7)).count()
    buyer_visit_30 =  user_info.filter(is_seller=False, is_buyer=True).filter(user_id__last_login__gte = current_time-timedelta(days=30)).count()
    buyer_visit_90 =  user_info.filter(is_seller=False, is_buyer=True).filter(user_id__last_login__gte = current_time-timedelta(days=90)).count()

    both_visit_7  =  user_info.filter(is_seller=True, is_buyer=True).filter(user_id__last_login__gte = current_time-timedelta(days=7)).count()
    both_visit_30 =  user_info.filter(is_seller=True, is_buyer=True).filter(user_id__last_login__gte = current_time-timedelta(days=30)).count()
    both_visit_90 =  user_info.filter(is_seller=True, is_buyer=True).filter(user_id__last_login__gte = current_time-timedelta(days=90)).count()

    pro_visit_7  =  user_info.filter(is_professional=True).filter(user_id__last_login__gte = current_time-timedelta(days=7)).count()
    pro_visit_30 =  user_info.filter(is_professional=True).filter(user_id__last_login__gte = current_time-timedelta(days=30)).count()
    pro_visit_90 =  user_info.filter(is_professional=True).filter(user_id__last_login__gte = current_time-timedelta(days=90)).count()

    nonuser_visit_7  =  user_info.filter(is_seller=False, is_buyer=False, is_professional=False).filter(user_id__last_login__gte = current_time-timedelta(days=7)).count()
    nonuser_visit_30 =  user_info.filter(is_seller=False, is_buyer=False, is_professional=False).filter(user_id__last_login__gte = current_time-timedelta(days=0)).count()
    nonuser_visit_90 =  user_info.filter(is_seller=False, is_buyer=False, is_professional=False).filter(user_id__last_login__gte = current_time-timedelta(days=90)).count()


    context = {

    'overall_users' : users_past_all,
    'new_users_7' : users_past_7,
    'new_users_30' : users_past_30,
    'new_users_90' : users_past_90,

    'overall_artists' : artist_past_all,
    'new_artists_7' : artist_past_7,
    'new_artists_30' : artist_past_30,
    'new_artists_90' : artist_past_90,

    'overall_buyer' : buyer_past_all,
    'new_buyer_7' : buyer_past_7,
    'new_buyer_30' : buyer_past_30,
    'new_buyer_90' : buyer_past_90,

    'overall_both' : both_past_all,
    'new_both_7' : both_past_7,
    'new_both_30' : both_past_30,
    'new_both_90' : both_past_90,

    'overall_pro' : pro_past_all,
    'new_pro_7' : pro_past_7,
    'new_pro_30' : pro_past_30,
    'new_pro_90' : pro_past_90,

    'overall_message' : message_past_all,
    'new_message_7' : message_past_7,
    'new_message_30' : message_past_30,
    'new_message_90' : message_past_90,

    'artist_message_all' : artist_message_all,
    'artist_message_7'  : artist_message_7,
    'artist_message_30' : artist_message_30,
    'artist_message_90' : artist_message_90,

    'buyer_message_all' : buyer_message_all,
    'buyer_message_7'  : buyer_message_7,
    'buyer_message_30' : buyer_message_30,
    'buyer_message_90' : buyer_message_90,


    'overall_post' : post_past_all,
    'new_post_7' : post_past_7,
    'new_post_30' : post_past_30,
    'new_post_90' : post_past_90,

    'overall_hold' : order_hold_past_all,
    'overall_hold_total' : order_hold_past_all_total["amount_total__sum"],
    'new_hold_7' : order_hold_past_7,
    'new_hold_7_total' : order_hold_past_7_total["amount_total__sum"],
    'new_hold_30' : order_hold_past_30,
    'new_hold_30_total' : order_hold_past_30_total["amount_total__sum"],
    'new_hold_90' : order_hold_past_90,
    'new_hold_90_total' : order_hold_past_90_total["amount_total__sum"],

    'overall_accept' : accepted_past_all,
    'overall_accept_total' : accepted_past_all_total['amount_total__sum'],
    'new_accept_7' : accepted_past_7,
    'new_accept_7_total' : accepted_past_7_total['amount_total__sum'],
    'new_accept_30' : accepted_past_30,
    'new_accept_30_total' : accepted_past_30_total['amount_total__sum'],
    'new_accept_90' : accepted_past_90,
    'new_accept_90_total' : accepted_past_90_total['amount_total__sum'],

    'overall_tracking' : tracking_provided_past_all,
    'overall_tracking_total' : tracking_provided_past_all_total['price__sum'],
    'new_tracking_7' : tracking_provided_past_7,
    'new_tracking_7_total' : tracking_provided_past_7_total['price__sum'],
    'new_tracking_30' : tracking_provided_past_30,
    'new_tracking_30_total' : tracking_provided_past_30_total['price__sum'],
    'new_tracking_90' : tracking_provided_past_90,
    'new_tracking_90_total' : tracking_provided_past_90_total['price__sum'],

    'total_visit_7':  total_visit_7,
    'total_visit_30': total_visit_30,
    'total_visit_90': total_visit_90,

    'artist_visit_7':artist_visit_7,
    'artist_visit_30':artist_visit_30,
    'artist_visit_90':artist_visit_90,

    'both_visit_7': both_visit_7,
    'both_visit_30':both_visit_30,
    'both_visit_90':both_visit_90,

    'buyer_visit_7':  buyer_visit_7,
    'buyer_visit_30':buyer_visit_30,
    'buyer_visit_90':buyer_visit_90,

    'pro_visit_7' :pro_visit_7,
    'pro_visit_30':pro_visit_30,
    'pro_visit_90':pro_visit_90,

    'nonuser_visit_7':nonuser_visit_7,
    'nonuser_visit_30':nonuser_visit_30,
    'nonuser_visit_90':nonuser_visit_90,


    }
    return render(request, 'custom_admin/stats.html', context)

class StatsAdmin(admin.ModelAdmin):
    model = Stats
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('custom/', stats_custom_view, name=view_name),
        ]




class AccountRegister(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_editable = ['featured_artist','company_email_verified']
    list_display = ['user', 'featured_artist', 'joined' , 'phone','has_stripe' , 'instagram_username', 'referred_by', 'is_professional', 'is_buyer', 'is_seller', 'company_email_verified', 'company_website', 'company_email']
    list_filter = ('is_professional', 'featured_artist' ,'is_buyer', 'is_seller','company_email_verified', 'referred_by', 'num_of_referrals', 'country')

    def joined(self, obj):
        return obj.user.date_joined

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'date_joined', 'email', 'first_name', 'last_name', 'is_staff') # Added last_login

class UserInfoInline(admin.StackedInline):
    model = UserInfo
    fields = ('instagram_username', 'phone')
    fk_name = 'user'


class MyUserAdmin(UserAdmin):
    inlines = [UserInfoInline,]
    list_display = ('username','date_joined','phone_number', 'instagram','email', 'first_name', 'last_name', 'is_staff',)

 
    def instagram(self, obj):
        user_info = UserInfo.objects.get(user=obj)
        return user_info.instagram_username

    def phone_number(self, obj):
        user_info = UserInfo.objects.get(user=obj)
        return user_info.phone



class CategoryAdmin(admin.ModelAdmin):
    list_editable = ['image',]
    list_display = ['category_name', 'image']


class ToCAdmin(admin.ModelAdmin):
    list_display = ['content', 'date']
    
    

admin.site.register(StripeInfo, StripeInfoAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(BioSearch, BioSearchAdmin)
admin.site.register(UserSearch, UserSearchAdmin)
admin.site.register(ArticleEdit, ArticleAdmin)
admin.site.unregister(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, MyUserAdmin)
admin.site.register(UserInfo, AccountRegister) 
admin.site.register(ArtistStatement)
admin.site.register(FeaturedWork)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(TermsAndConditions, ToCAdmin)
admin.site.register(Accomplishment)
admin.site.register(Exhibition)
admin.site.register(HeaderImage)
admin.site.register(UserFollowing)
admin.site.register(CreditDonation)

