from django.contrib import admin
from .models import UserPreference, UserPreferenceCategory, UserPreferenceStyle, AdvisoryPageData

# Register your models here.

class UserPreferenceSurvey(admin.ModelAdmin):
	list_display = ['id', 'image', 'value']
	list_editable = ['image', 'value']
	

class UserPreferenceCategorySurvey(admin.ModelAdmin):
	list_display = ['id', 'image', 'value']
	list_editable = ['image', 'value']


class UserPreferenceStyleSurvey(admin.ModelAdmin):
	list_display = ['id', 'image', 'value']
	list_editable = ['image', 'value']

class AdvisoryPageDataSurvey(admin.ModelAdmin):
	list_display = ['category_sculpture', 'category_photography', 'category_drawing', \
					'category_painting', 'style_abstract', 'style_blackAndWhite', \
					'style_figurative', 'style_landscape', 'style_minimalist', \
					'style_popArt', 'style_portraiture', 'style_street', 'style_other', \
					'preferred_pieces', 'orientation_horizontal', 'orientation_vertical', \
					'orientation_square', 'size_oversize', 'size_large', 'size_medium', 
					'size_small', 'budget', 'firstName', 'lastName', 'email', \
					'phone', 'notes', 'newsletterSubscription']


admin.site.register(UserPreference, UserPreferenceSurvey) 
admin.site.register(UserPreferenceCategory, UserPreferenceCategorySurvey)
admin.site.register(UserPreferenceStyle, UserPreferenceStyleSurvey) 
admin.site.register(AdvisoryPageData, AdvisoryPageDataSurvey)