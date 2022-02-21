# Standard library imports
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.db import transaction
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
import logging


# Related third party imports
from bs4 import BeautifulSoup


# Local application/library specific imports
from exceptions.customs import UserNameExistsException
from products.utils import decode_base64_file
from accounts import choices
from products import choices as product_choices
from accounts.models import UserInfo
from .models import Channel, Comment, Post, Like
from .utils import get_liked_post
from . import email_template
from accounts.email import create_message, create_attachment, read_image, sendgrid_send_email
from accounts.utils import clear_messages


@login_required
def create_post(request):

	if messages is not None:
		clear_messages = messages.get_messages(request)
		if clear_messages:
			for message in clear_messages:
				pass
	try:
		content = request.POST['content-data'].strip()
		channel_name = request.POST['channel-name'].strip()
		channel_id = Channel.objects.filter(name=channel_name)

		if channel_id.count() < 1:
			messages.error(request, "Please choose a channel")
			return redirect('create_page')

		if len(content) == 0:
			messages.error(request, "No content to post")
			return redirect('create_page')

		if len(request.POST['content-title']) == 0:
			messages.error(request, "Title is required")
			return redirect('create_page')

		user = UserInfo.objects.filter(user=request.user)[0]
		soup = BeautifulSoup(content)

		img_data = None

		if(len(soup.findAll('img')) > 0):
			img_data = soup.findAll('img')[0]['src']

			for tag in soup('img'):
				tag.decompose()

		content = soup.prettify()

		obj = Post(question=content, user=user, channel_id=channel_id[0], img=decode_base64_file(img_data), title=request.POST['content-title'])
		obj.save()
		messages.success(request, 'Posted successfully')
		return redirect('post_details', obj.id)
	except UserNameExistsException as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, "Unable to post.")
		return redirect('create_page')

@login_required
def create_page(request):
	channels_obj = Channel.objects.filter(show=True)
	return render(request, 'community/post_form.html', {'channel' : channels_obj,'category' : product_choices.category,})



def start(request):
	""" This method is used to retrive all the posts.
		It uses
	"""
	try:
		clear_messages(messages, request)
		page = request.GET.get('page', 1)
		channel_obj = Channel.objects.all()
		post_obj = Post.objects.order_by('-created_date')

		paginator = Paginator(post_obj, 10)
		total_pages = paginator.num_pages
		if int(page) > total_pages:
			page = 1
		paged_post_obj = paginator.page(page)

		liked_obj = None
		if request.user.is_authenticated:
			current_user = UserInfo.objects.get(user=request.user)
			liked_obj = get_liked_post(paged_post_obj, current_user)
			liked_obj = [str(i.post_id.id) for i in liked_obj]

		post_with_like_info = []

		if liked_obj is not None:
			for paged_single in paged_post_obj:
				temp = {}
				temp['obj'] = paged_single

				if str(paged_single.id) in liked_obj:

					temp['liked'] = True
					post_with_like_info.append(temp)
				else:


					temp['liked'] = False
					post_with_like_info.append(temp)
		else:
			for paged_single in paged_post_obj:
				temp = {}
				temp['obj'] = paged_single
				temp['liked'] = False
				post_with_like_info.append(temp)

		context = {
			'all_required_posts' : post_with_like_info,
			'channels' : channel_obj,
			'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
			'total_pages': total_pages,
			'paginator' : paginator,
			'category' : product_choices.category,
		}

 
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {'category' : product_choices.category,}

	return render(request, 'community/index.html', context)


def specific(request, channelname):
	""" This method is used to retrive all the posts.
		It uses
	"""

	try:
		clear_messages(messages, request)
		page = request.GET.get('page', 1)
		channel_obj = Channel.objects.all()

		channel_specific = Channel.objects.filter(name = channelname.strip())

		if channel_specific.count() == 0:
			return render(request, 'community/index.html')

		post_obj = Post.objects.filter(channel_id=channel_specific[0]).order_by('-created_date')

		paginator = Paginator(post_obj, 10)
		total_pages = paginator.num_pages
		if int(page) > total_pages:
			page = 1
		paged_post_obj = paginator.page(page)

		liked_obj = None
		if request.user.is_authenticated:
			current_user = UserInfo.objects.get(user=request.user)
			liked_obj = get_liked_post(paged_post_obj, current_user)
			liked_obj = [str(i.post_id.id) for i in liked_obj]

		post_with_like_info = []

		if liked_obj is not None:
			for paged_single in paged_post_obj:
				temp = {}
				temp['obj'] = paged_single

				if str(paged_single.id) in liked_obj:

					temp['liked'] = True
					post_with_like_info.append(temp)
				else:


					temp['liked'] = False
					post_with_like_info.append(temp)
		else:
			for paged_single in paged_post_obj:
				temp = {}
				temp['obj'] = paged_single
				temp['liked'] = False
				post_with_like_info.append(temp)

		context = {
			'all_required_posts' : post_with_like_info,
			'channels' : channel_obj,
			'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
			'total_pages': total_pages,
			'category' : product_choices.category,
			'channel_name': channelname,
			'channel_desc' : channel_specific[0].desc,
			'paginator' : paginator,
		}

	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {'category' : product_choices.category,}

	return render(request, 'community/index.html', context)



def get_comments(request):
	try:
		if request.method == 'POST':
			post_id = request.POST['post_id'].strip()
			post_obj = Post.objects.get(id=post_id)
			comments = Comment.objects.filter(post_id=post_obj).filter(show=True).exclude(parent__isnull=False)
			data = []
			for comment in comments:
				temp = {}
				sub_comments = Comment.objects.filter(parent=str(comment.id)).exclude(show=False)
				temp['comment'] = comment.comment
				temp['subcomment'] = serializers.serialize('json', sub_comments)
				data.append(temp)

			return JsonResponse({'status':'success', 'data' : data}, status=200)
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
	return JsonResponse({'status':'fail'}, status=500)


@login_required
def add_comment(request):
	try:

		with transaction.atomic():
			if request.method == 'POST':
				post_id = request.POST['post_id'].strip()
				comment = request.POST['comment'].strip()

				if len(comment) > 0:
					user = UserInfo.objects.get(user=request.user)
					BASE_IMG_URL = settings.BASE_AWS_IMG_URL
					post_obj = Post.objects.get(id=post_id)
					post_obj.comment_count+=1
					post_obj.save()
					comment_obj = Comment(comment=comment, user=user, post_id=post_obj)
					comment_obj.save()

					try:
						if request.user != post_obj.user.user:
							from_email = settings.FROM_EMAIL
							to_email = post_obj.user.user.email
							if len(post_obj.title) > 0:
								subject='New comment on ' + post_obj.title
							else:
								subject='New comment on your post'


							commented_by_name = request.user.first_name + ' ' + request.user.last_name
							link_to_post = settings.HOST_BASE_URL + 'community/post/' + str(post_obj.id)

							# TODO : PUT EMAIL CODE HERE
							IMG_1_PATH = settings.BASE_DIR + '/bidgala/static/img/email/logo_white_bg.png'
							data1 = read_image(IMG_1_PATH)
							IMG_facebook_PATH = settings.BASE_DIR + '/bidgala/static/img/email/facebook.png'
							data_facebook = read_image(IMG_facebook_PATH)
							IMG_twitter_PATH = settings.BASE_DIR + '/bidgala/static/img/email/twitter.png'
							data_twitter = read_image(IMG_twitter_PATH)
							IMG_instagram_PATH = settings.BASE_DIR + '/bidgala/static/img/email/instagram.png'
							data_instagram = read_image(IMG_instagram_PATH)

							IMG_linkedin_PATH = settings.BASE_DIR + '/bidgala/static/img/email/linkedin.png'
							data_linkedin = read_image(IMG_linkedin_PATH)
							IMG_pinterest_PATH = settings.BASE_DIR + '/bidgala/static/img/email/pinterest.png'
							data_pinterest = read_image(IMG_pinterest_PATH)
							message_ = create_message(to_email, subject, email_template.receiveComment(post_obj.title if len(post_obj.title) > 0 else "your post", link_to_post, comment, commented_by_name))

							attachment1 = create_attachment(data1, 'img/png', 'logo.png', 'logo')
							attachment_facebook = create_attachment(data_facebook, 'img/jpg', 'facebook.jpg', 'facebook')
							attachment_twitter = create_attachment(data_twitter, 'img/jpg', 'twitter.jpg', 'twitter')
							attachment_instagram = create_attachment(data_instagram, 'img/jpg', 'instagram.jpg', 'instagram')
							attachment_linkedin = create_attachment(data_linkedin, 'img/jpg', 'linkedin.jpg', 'linkedin')
							attachment_pinterest = create_attachment(data_pinterest, 'img/jpg', 'pinterest.jpg', 'pinterest')
							message_.add_attachment(attachment1)
							message_.add_attachment(attachment_facebook)
							message_.add_attachment(attachment_twitter)
							message_.add_attachment(attachment_instagram)
							message_.add_attachment(attachment_linkedin)
							message_.add_attachment(attachment_pinterest)

							try:
								sendgrid_send_email(message_)
							except Exception as e:
								logging.getLogger("error_logger").error(str(e))

					except Exception as e:
						logging.getLogger("error_logger").error(str(e))

					if user.profile_img:
						profile_img = BASE_IMG_URL + str(user.profile_img)
					else:
						profile_img = static('img/profile-icon.png')

					data = [comment_obj.comment, request.user.username, comment_obj.created_date, profile_img, comment_obj.id, comment_obj.post_id.id]

					return JsonResponse({'status':'success', 'data' : data}, status=200)
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		messages.error(request, 'Comment could not be added.')

		return JsonResponse({'status':'fail'}, status=500)



@login_required
def delete_post(request, postid):
	try:
		clear_messages(messages, request)
		if request.method == 'POST':
			# post_id = request.POST('post_id').strip()
			user = UserInfo.objects.get(user=request.user)
			Post.objects.get(user=user, id=postid)
			post_obj = Post.objects.get(user=user, id=postid)
			post_obj.delete()
			messages.success(request, 'Post deleted successfully.')

			return redirect('all_post')
	except Exception as e:
		messages.error(request, 'Post could not be deleted.')
		logging.getLogger("error_logger").error(str(e))

		return redirect('post_details', postid)



@login_required
def like_post(request):
	try:
		clear_messages(messages, request)
		with transaction.atomic():
			if request.method == 'POST':
				action_taken = ''
				post_id = request.POST['post_id']
				user = UserInfo.objects.get(user=request.user)
				post_obj = Post.objects.get(id=post_id)
				like_history_obj = Like.objects.filter(user=user, post_id=post_obj)


				if like_history_obj.count() > 0:
					like_history_obj.delete()

					if post_obj.like_count > 0:
						post_obj.like_count -=1
						post_obj.save()
						action_taken = 'decrement'
				else:
					like_obj = Like(user=user, post_id=post_obj)
					like_obj.save()
					post_obj.like_count +=1
					post_obj.save()
					action_taken = 'increment'

				return JsonResponse({'status':'success', 'result': action_taken ,  'postid': post_id}, status=200)

	except UserNameExistsException as e:
		logging.getLogger("error_logger").error(str(e))

		return JsonResponse({'status':'fail', 'message':'Something went wrong. Please try again later.'}, status=500)



def post_details(request, postid):
	try:
		clear_messages(messages, request)
		is_liked = False
		comments = Comment.objects.filter(post_id=postid, show=True).order_by("-created_date")

		if request.user.is_authenticated:
			user_obj = UserInfo.objects.filter(user=request.user)[0]
			is_liked = True if get_liked_post([postid], str(user_obj.id)).count() > 0 else False

		post = Post.objects.get(id=postid)
		context = {
			'post': post,
			'BASE_IMG_URL' : settings.BASE_AWS_IMG_URL,
			'comments': comments,
			'category' : product_choices.category,
			'is_liked' : is_liked,
		}
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {}

	return render(request, 'community/post_details.html', context)



@login_required
def delete_comment(request, pid, cid):
	try:
		clear_messages(messages, request)
		with transaction.atomic():
			user = UserInfo.objects.get(user=request.user)
			comment = Comment.objects.filter(id=cid)[0]
			if user == comment.user:
				comment.show = False
				comment.save()
				comment.post_id.comment_count = comment.post_id.comment_count - 1
				comment.post_id.save()

	except Exception as e:
		messages.error(request, 'Comment could not be deleted.')
		logging.getLogger("error_logger").error(str(e))


	return redirect('post_details', postid=pid)
