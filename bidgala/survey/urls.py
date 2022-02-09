from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.survey, name="survey"),
	path('options/user-preference-options', views.getUserPreferenceOptions),
	path('options/user-preference-category-options', views.getUserPreferenceCategoryOptions),
	path('options/user-preference-style-options', views.getUserPreferenceStyleOptions),
	path('submit/advisory-data', views.submitAdvisoryData),
]