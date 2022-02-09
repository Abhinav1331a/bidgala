from django.urls import path, include
from . import views

# TODO : Split accept and decline methods and then change url

urlpatterns = [
	path('', views.orders, name='orders'),
	path('acceptordeclineorder', views.accept_or_decline_order, name='accept_or_decline_order'),
	path('submit-tracking', views.submit_tracking, name='submit_tracking'),
	path('inquiry', views.inquiry, name='inquiry'),
	path('inquiry-accept', views.inquiry_accept, name="inquiry_accept"),
	path('inquiry-delete', views.inquiry_delete, name="inquiry_delete"),
]