from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
# from accounts.views import CustomFormSignupView
from django.conf.urls import handler404
from django.conf.urls import handler500
import pages
from . import views

urlpatterns = [
    path('NewsLetter', views.NewsLetter, name='NewsLetter'),
]
