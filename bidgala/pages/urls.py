from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('demo', views.index_demo, name='index_demo'),
	path('about', views.about, name='about'),
	path('privacy', views.privacy, name='privacy'),
	path('cookie', views.cookie, name='cookie'),
	path('pack-guide', views.pack_guide, name="pack_guide"),
	path('bidgala101', views.bidgala_101, name="bidgala101"),
	path('directory', views.directory, name='directory'),
	# path('partners',views.partners,name='partners')
	path('terms-and-conditions', views.terms_of_conditions, name="terms_and_conditions"),
	path('help', views.help, name="help"),
	path('faq', views.faq, name="faq"),
	path('advisory', views.advisory, name="advisory"),
	
]