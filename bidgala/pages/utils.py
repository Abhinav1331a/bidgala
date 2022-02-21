from community.models import Channel
from discover.models import Article
from accounts.models import UserInfo, Category

def get_featured_artist():
	""" This method is used to return the featured artist
	"""
	return UserInfo.objects.filter(featured_artist=True)


def get_latest_article(count_):
	""" This method is used to return the latest articles
	"""
	obj = Article.objects.order_by('-created_date')
	return obj if obj.count() <= count_ else obj[0:count] 


def get_channel():
	channel_obj = Channel.objects.all()
	return channel_obj


def get_category():
	category_obj = Category.objects.all()
	return category_obj