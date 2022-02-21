from rest_framework import serializers
from .models import Product
from accounts.models import UserInfo
from django.contrib.auth.models import User



class ProductAndUserSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.id', read_only=True)
	owner_first_name = serializers.ReadOnlyField(source='owner.user.first_name', read_only=True)
	owner_last_name = serializers.ReadOnlyField(source='owner.user.last_name', read_only=True)
	owner_message_id = serializers.ReadOnlyField(source='owner.id', read_only=True)
	

	class Meta:
		model = Product
		fields = [
			'id',
			'art_title',
			'art_desc',
			'tags',
			'height',
			'depth',
			'width',
			'dim_measure',
			'category',
			'subcategory',
			'price',
			'shipping_price_us',
			'shipping_price_can',
			'shipping_price_uk',
			'shipping_price_asia',
			'shipping_price_aunz',
			'shipping_price_europe',
			'shipping_price_other',
			'show_shipping_price_us',
			'show_shipping_price_can',
			'show_shipping_price_uk',
			'show_shipping_price_asia',
			'show_shipping_price_aunz',
			'show_shipping_price_europe',
			'show_shipping_price_other',
			'color',
			'color_1',
			'color_2',
			'color_3',
			'color_4',
			'owner',
			'owner_first_name',
			'owner_last_name',
			'owner_message_id',
			'date',
			'image',
			'additional_image_1',
			'additional_image_2',
			'additional_image_3',
			'additional_image_4',
			'sold',
			'available',
			'is_signed',
			'is_framed_or_hang',
			'styles',
			'materials',
			'curator_pick',
			'comment_count',
			'favourite_count',
		]




class ProductSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Product
		fields = [
			'id',
			'art_title',
			'art_desc',
			'tags',
			'height',
			'depth',
			'width',
			'dim_measure',
			'category',
			'subcategory',
			'price',
			'shipping_price_us',
			'shipping_price_can',
			'shipping_price_uk',
			'shipping_price_asia',
			'shipping_price_aunz',
			'shipping_price_europe',
			'shipping_price_other',
			'show_shipping_price_us',
			'show_shipping_price_can',
			'show_shipping_price_uk',
			'show_shipping_price_asia',
			'show_shipping_price_aunz',
			'show_shipping_price_europe',
			'show_shipping_price_other',
			'color',
			'color_1',
			'color_2',
			'color_3',
			'color_4',
			'owner',
			'date',
			'image',
			'additional_image_1',
			'additional_image_2',
			'additional_image_3',
			'additional_image_4',
			'sold',
			'available',
			'is_signed',
			'is_framed_or_hang',
			'styles',
			'materials',
			'curator_pick',
			'comment_count',
			'favourite_count',
			
		]
		extra_kwargs = {
			'id' : {'required' : False},
			'additional_image_1' : {'required' : False},
			'additional_image_2' : {'required' : False},
			'additional_image_3' : {'required' : False},
			'additional_image_4' : {'required' : False},
			'sold' : {'required' : False},
			'available' : {'required' : False},
			'curator_pick' : {'required' : False},
			'comment_count' : {'required' : False},
			'favourite_count' : {'required' : False},
			'owner' : {'required' : False},
			'date' : {'required' : False},
			'tags' : {'required' : False},
			'depth' : {'required' : False},

		}