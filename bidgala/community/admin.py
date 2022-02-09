from django.contrib import admin
from .models import Channel, Post, Comment, Like

# Register your models here.
class ChannelRegister(admin.ModelAdmin):
	list_display = ['id', 'name', 'img', 'show', 'created_by']
	list_filter = ['name', 'show', 'created_by']
	list_editable = ('img', 'show')
	list_per_page = 25


class PostRegister(admin.ModelAdmin):
	list_display = ['id', 'title', 'question', 'img', 'user', 'channel_id', 'like_count', 'comment_count', 'show', 'created_date']
	list_filter = ['user', 'channel_id', 'like_count', 'comment_count', 'show', 'created_date']
	list_editable = ('img', 'show')
	list_per_page = 25

admin.site.register(Channel, ChannelRegister)   
admin.site.register(Post, PostRegister) 
admin.site.register(Comment) 
admin.site.register(Like) 