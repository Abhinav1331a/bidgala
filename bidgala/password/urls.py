from django.urls import path, include

from . import views

urlpatterns = [
	path('forgot', views.forgot_password_page, name='forgot'),
	path('submit-email', views.submit_email, name='submit_email'),
	path('set-password/<str:key>', views.set_password_page, name='set_password'),
	path('change-password', views.change_password, name='change_password'),
	]