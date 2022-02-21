from django.contrib import admin
from .models import HomePage

# Register your models here.

class HomePageAdmin(admin.ModelAdmin):
	list_display = ['id', 'image', 'value']
	list_editable = ['image', 'value']


admin.site.register(HomePage, HomePageAdmin) 