from django.shortcuts import render, redirect
from .models import Category, Article, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.db import transaction
from django.http import JsonResponse
from accounts.models import UserInfo
from django.conf import settings
from django.contrib import messages


from pygram import PyGram

# Logging
import logging 
from products import choices as product_choices
from accounts import choices



# Create your views here.
def index(request):
	""" This method is used to render the discover page.

	Args:
		request: The request object.

	Returns:
		It renders the discover.html page.

	"""
	# pygram = PyGram()
	# ig_posts = pygram.get_posts('bidgala', limit=12)
	try:
		page = request.GET.get('page', 1)
		categories = Category.objects.all()
		articles = Article.objects.order_by('-created_date')

		paginator = Paginator(articles, 10)
		total_pages = paginator.num_pages
		if int(page) > total_pages:
			page = 1
		paged_article_obj = paginator.page(page)

		context ={
			'articles': paged_article_obj,
			'categories': categories,
			'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
			'category' : product_choices.category,
			# "ig_posts" : ig_posts,
		}
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {}
 
	return render(request, "discover/discover.html", context)
	

def category_page(request, category):
	""" This method is used to render category page.

	Args:
		request: The request object.

	Returns:
		It renders the discover.html page.

	"""
	try:
		page = request.GET.get('page', 1)
		categories = Category.objects.all()

		specific_category = Category.objects.filter(name = category)

		if specific_category.count() == 0:
			return render(request, 'discover/discover.html')

		articles = Article.objects.filter(category=specific_category[0]).order_by('-created_date')
		
		paginator = Paginator(articles, 10)
		
		total_pages = paginator.num_pages
		if int(page) > total_pages:
			page = 1
		paged_article_obj = paginator.page(page)

		context = {
			'articles' : paged_article_obj,
			'categories' : categories,
			'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
			'category' : product_choices.category,
		}
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {}

	return render(request, "discover/discover.html", context)



def article_details(request, slug):
	""" This method is used to render the article page.

	Args:
		request: The request object.

	Returns:
		It renders the article.html page.

	"""
	try: 
		article_obj = Article.objects.get(slug=slug)
		comments = Comment.objects.filter(article_id=article_obj.id, show=True).order_by("-created_date")



		context = {
			'article': article_obj,
			'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
			'comments': comments,
			'category' : product_choices.category,
		}
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {}

	return render(request, "discover/article.html", context)


@login_required
def add_comment(request):
	try:
		with transaction.atomic():
			if request.method == 'POST':
				article_id = request.POST['article_id'].strip()
				comment = request.POST['comment'].strip()
				
				if len(comment) > 0:
					user = UserInfo.objects.get(user=request.user)
					BASE_IMG_URL = settings.BASE_AWS_IMG_URL
					article_obj = Article.objects.get(id=article_id)
					article_obj.comment_count+=1
					article_obj.save()
					comment_obj = Comment(body=comment, user=user, article_id=article_obj)
					comment_obj.save()
					
					if user.profile_img:
						profile_img = BASE_IMG_URL + str(user.profile_img)
					else: 
						profile_img = static('img/profile-icon.png')

					data = [comment_obj.body, request.user.username, comment_obj.created_date, profile_img, comment_obj.id, article_obj.slug]

					return JsonResponse({'status':'success', 'data' : data}, status=200)
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Comment could not be added.')

		return JsonResponse({'status':'fail'}, status=500)


@login_required
def delete_comment(request, article_slug, comment_id):
	try:
		with transaction.atomic():
			user = UserInfo.objects.get(user=request.user)
			comment = Comment.objects.filter(id=comment_id)[0]
			if user == comment.user:
				comment.show = False
				comment.save()
				comment.article_id.comment_count = comment.article_id.comment_count - 1
				comment.article_id.save()
			
	except Exception as e:
		messages.error(request, 'Comment could not be deleted.')
		logging.getLogger("error_logger").error(str(e))


	
	return redirect('article_details', slug=article_slug)