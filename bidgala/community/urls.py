# Standard library imports
from django.urls import path, include

# Related third party imports

# Local application/library specific imports
from . import views

urlpatterns = [
	path('posts', views.start, name="all_post"),
	path('posts/<str:channelname>/', views.specific, name="specific"),
	path('create', views.create_page, name="create_page"),
	path('create-post', views.create_post, name="create_post"),
	path('add-comment', views.add_comment, name="add_comment"),
	path('add-like', views.like_post, name="like_post"),
	path('delete-post/<str:postid>', views.delete_post, name="delete_post"),
	path('post/<str:postid>', views.post_details, name="post_details"),
	path('delete-comment/<str:pid>/<str:cid>', views.delete_comment, name="delete_comment"),
	]