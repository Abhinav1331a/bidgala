# Standard library imports
from django.urls import path, include

# Related third party imports

# Local application/library specific imports
from . import views

urlpatterns = [
	path('pay/', views.pay_influencer),
	]