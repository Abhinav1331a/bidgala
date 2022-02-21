from django.contrib import admin

from .models import Article, Category, Comment, ArticleImage

# Register your models here.

class CategoryRegister(admin.ModelAdmin):
	list_display = ['id', 'name', 'show', 'created_by']
	list_filter = ['name', 'show', 'created_by']
	list_per_page = 25


class ArticleRegister(admin.ModelAdmin):
	list_display = ['id', 'title', 'img', 'user', 'category', 'like_count', 'comment_count', 'show', 'created_date', 'slug', 'main_img_source']
	list_filter = ['user', 'category', 'like_count', 'comment_count', 'show', 'created_date']
	list_editable = ('img', 'show')
	list_per_page = 25

class ArticleImageRegister(admin.ModelAdmin):
	list_display = ['id', 'full_img_path', 'created_date', 'main_image']
	list_filter = ['id']

	def full_img_path(self, item):
		from django.shortcuts import resolve_url
		from django.contrib.admin.templatetags.admin_urls import admin_urlname
		from django.utils.html import format_html

		return format_html('{full_url}'.format(full_url=item.base + str(item.img)))


admin.site.register(Category, CategoryRegister)   
admin.site.register(Article, ArticleRegister) 
admin.site.register(Comment)
admin.site.register(ArticleImage, ArticleImageRegister)