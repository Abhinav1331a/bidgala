from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	path('', views.index, name='discover'),
    path('', views.index, name='blog'),
    path('category/<str:category>', views.category_page, name="category_page"),
    path('add-comment', views.add_comment, name="add_comment"),
    path('delete-comment/<str:article_slug>/<str:comment_id>', views.delete_comment, name="delete_comment"),
	path('<slug:slug>', views.article_details, name='article_details'),
]


 