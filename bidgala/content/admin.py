from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
	list_display = ('subject',)
	list_display_links = ('subject', )
	list_filter = ('subject',)
	list_per_page = 25
	search_fields = ('subject',)



admin.site.register(Content, ContentAdmin) 