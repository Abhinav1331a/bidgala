from django.contrib import admin
from .models import Stripe, Orders, OrderHold
from django.conf import settings

class OrdersRegister(admin.ModelAdmin):
	list_display = ['id', 'order_date', 'display_img' , 'art_details', 'purchased', 'tracking_number']
	list_filter = ['id', 'order_date',  'purchased']
	list_per_page = 25
	search_fields = ['id']
	

	def art_details(self, item):
		from django.shortcuts import resolve_url
		from django.contrib.admin.templatetags.admin_urls import admin_urlname
		from django.utils.html import format_html
		
		
		return format_html('<p>Price: <b>{price}</b><br/>Seller Name: <b>{s_name}</b> <br/>Seller Email: <b>{s_email}</b> <br/>Seller Insta: <b>{s_insta}</b><br/><br/>Buyer Name: <b>{b_name}</b><br/>Buyer Email: <b>{b_email}</b><br/>Buyer Insta: <b>{b_insta}</b></p>'.format(price=item.order_hold.amount_total, s_name=item.order_hold.seller.user.first_name + ' ' + item.order_hold.seller.user.last_name, s_email=item.order_hold.seller.user.email, s_insta=item.order_hold.seller.instagram_username, b_name=item.order_hold.buyer.user.first_name + ' ' + item.order_hold.buyer.user.last_name, b_email=item.order_hold.buyer.user.email, b_insta=item.order_hold.buyer.instagram_username,))


	def display_img(self, item):
		from django.shortcuts import resolve_url
		from django.contrib.admin.templatetags.admin_urls import admin_urlname
		from django.utils.html import format_html
		return format_html('<img src={domain}{img} style="width:150px; height:150px">'.format(domain=settings.BASE_AWS_IMG_URL , img=item.order_hold.product.image))


class OrderHoldRegister(admin.ModelAdmin):
	list_display = ['id', 'created_timestamp', 'display_img' , 'art_details', 'accepted', 'accepted_timestamp' ,'declined','declined_timestamp', 'has_tracking']
	list_filter = ['id', 'created_timestamp', 'accepted', 'accepted_timestamp' ,'declined','declined_timestamp', 'has_tracking']
	list_per_page = 25
	search_fields = ['id']
	

	def art_details(self, item):
		from django.shortcuts import resolve_url
		from django.contrib.admin.templatetags.admin_urls import admin_urlname
		from django.utils.html import format_html
		
		
		return format_html('<p>Price: <b>{price}</b><br/>Seller Name: <b>{s_name}</b> <br/>Seller Email: <b>{s_email}</b> <br/>Seller Insta: <b>{s_insta}</b><br/><br/>Buyer Name: <b>{b_name}</b><br/>Buyer Email: <b>{b_email}</b><br/>Buyer Insta: <b>{b_insta}</b></p>'.format(price=item.amount_total, s_name=item.seller.user.first_name + ' ' + item.seller.user.last_name, s_email=item.seller.user.email, s_insta=item.seller.instagram_username, b_name=item.buyer.user.first_name + ' ' + item.buyer.user.last_name, b_email=item.buyer.user.email, b_insta=item.buyer.instagram_username,))


	def display_img(self, item):
		from django.shortcuts import resolve_url
		from django.contrib.admin.templatetags.admin_urls import admin_urlname
		from django.utils.html import format_html
		return format_html('<img src={domain}{img} style="width:150px; height:150px">'.format(domain=settings.BASE_AWS_IMG_URL , img=item.product.image))




admin.site.register(Stripe)
admin.site.register(OrderHold, OrderHoldRegister)
admin.site.register(Orders, OrdersRegister)

