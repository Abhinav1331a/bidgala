from cached_property import cached_property_with_ttl
from cached_property import cached_property
from products.models import Product
from accounts.models import Category
from accounts.models import SubCategory
from accounts.models import Material
from accounts.models import Style


class CachedProduct(object):
	@cached_property_with_ttl(ttl=600)
	def cached_all_products(self):
		return Product.objects.all() 


class CachedCategory(object):
	@cached_property
	def cached_all_category(self):
		return Category.objects.all()


class CachedSubCategory(object):
	@cached_property
	def cached_all_subcategory(self):
		return SubCategory.objects.all()


class CachedMaterial(object):
	@cached_property
	def cached_all_material(self):
		return Material.objects.all()


class CachedStyle(object):
	@cached_property
	def cached_all_style(self):
		return Style.objects.all()