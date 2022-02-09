# Standard library imports
from django.urls import path, include, re_path

# Related third party imports

# Local application/library specific imports
from . import views

urlpatterns = [
	re_path(r"^(?P<username>[\w.@+-]+)/$", views.thread, name="get_thread"),
	path("contacts", views.contacts, name="show_contacts"),
	path("message-page-order", views.get_messages, name="message_page_order"),
	]