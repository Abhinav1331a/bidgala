from django.urls import path, include
from . import views

urlpatterns = [	
	path('add-art', views.add_art, name='add_art'),
	path('my-art', views.my_art, name='my_art'),
	path('delete-art', views.delete_art, name='delete_art'),
	path('edit-art', views.edit_art, name='edit_art'),

	path('product_view/<str:id>/', views.product_view, name='product_view'),
	path('search/<str:type_>/<str:value>/', views.show_search, name="show_search"),
	path('filter-art', views.filter_art, name="filter_art"),
	path('search-result/',views.get_search_results, name="search"),
	path('favourite/', views.set_favourite_product, name="favourite_product"),
	path('wish-list', views.get_user_wish_list, name="wish_list"),

	path('add-comment', views.add_comment, name="add_comment_product"),
    path('delete-comment/<str:product_id>/<str:comment_id>', views.delete_comment, name="delete_comment_product"),
	path('upload', views.art_upload_page, name='art_upload'),
    path('art-sold', views.art_sold),
    path('art-unsold', views.art_unsold),

    path('api/curator-pick', views.CuratorList.as_view()),
    path('api/product/<str:pk>', views.ProductDetail.as_view())
	]  