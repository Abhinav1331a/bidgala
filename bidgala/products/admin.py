from django.contrib import admin
from .models import Product
# Register your models here.

class ProductRegister(admin.ModelAdmin):
	raw_id_fields = ('owner',)
	list_display = ['id','art_title', 'owner_details' ,'owner', 'price', 'curator_pick', 'home_decor', 'structube', 'sold', 'available', 'date', 'main_image', 'additional_1_view', 'additional_2_view', 'additional_3_view', 'additional_4_view', 'category', 'subcategory']
	list_filter = ('owner', 'category', 'subcategory','date', 'sold', 'curator_pick', 'home_decor', 'structube', 'available')
	list_editable = ('curator_pick','home_decor', 'structube')
	list_per_page = 25
	search_fields = ['id']
	list_display_links = ["owner"]

	def owner_details(self, item):
		from django.shortcuts import resolve_url
		from django.contrib.admin.templatetags.admin_urls import admin_urlname
		from django.utils.html import format_html
		
		
		return format_html('<p>First Name: {first} <br/>Last Name: {last} <br/>Phone: {phone}<br/></p>'.format(first=item.owner.user.first_name, last=item.owner.user.last_name, phone=item.owner.phone))



admin.site.register(Product, ProductRegister)  