# Standard library imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from channels.consumer import AsyncConsumer
from django.core.paginator import Paginator
from datetime import datetime
from channels.db import database_sync_to_async
from django.templatetags.static import static
import asyncio
import logging

# Related third party imports
from ordered_set import OrderedSet

# Local application/library specific imports
from accounts.models import UserInfo
from .models import Conversation, Message
from products import choices as product_choices
from influencer.models import Influencer


@login_required
def get_messages(request):
	page = 1
	try:
		if request.method == 'POST':
			page =1 
			response = {'status':'success'}
			other_user_id = request.POST['user_id']
			

			datetime_object = request.POST['timestamp']

			#timestamp = timestamp.replace(',', '').replace('.', '').replace(' pm', 'PM').replace(' am', 'AM')
			#datetime_object = datetime.strptime(timestamp, '%b %d %Y %I:%M%p') 

			current_user = UserInfo.objects.get(user = request.user)
			other_user_obj = UserInfo.objects.get(id = other_user_id)
			thread_obj, is_created =  check_conversation(request.user, other_user_id)
			messages_conv = None

			# This message object is used to mark all messages as read.
			message_object = Message.objects.filter(conversation_id=thread_obj).exclude(origin_user=current_user)
			message_object.update(read=True)
			##
			contact_thread  = Conversation.objects.filter((Q(user_1=current_user) & Q(user_2=other_user_obj)) |  (Q(user_2=current_user) & Q(user_1=other_user_obj)))

			if contact_thread.count() > 0:
				if len(datetime_object) > 0:
					messages_conv = Message.objects.filter(conversation_id=contact_thread[0]).filter(timestamp__lt=datetime_object).order_by('-timestamp')
				else:
					messages_conv = Message.objects.filter(conversation_id=contact_thread[0]).order_by('-timestamp')
				paginator = Paginator(messages_conv, 10)
				paged_message = paginator.page(page)

				message_count = len(paged_message)
				temp_array = []
				for i in range(message_count-1, -1,-1):
					temp_dict = {}
					temp_dict['text'] = paged_message[i].message_text
					temp_dict['primary'] = True if paged_message[i].origin_user.user == request.user else False
					temp_dict['timestamp'] = paged_message[i].timestamp
					
					temp_array.append(temp_dict)

				response['messages'] = temp_array

				if other_user_obj.profile_img:
					profile_img = settings.BASE_AWS_IMG_URL + str(other_user_obj.profile_img)
				else: 
					profile_img = static('img/profile-icon.png')

				response['other_user_info'] = {
											'profile_img' : profile_img,
											'profile_link' : settings.HOST_BASE_URL + 'p/' + other_user_obj.user.username,
											'name' : other_user_obj.user.first_name + ' ' + other_user_obj.user.last_name
										}
			return JsonResponse(response, status=200)
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
	
	response = {'status':'fail'}
	return JsonResponse(response, status=500)


@login_required
def thread(request, username):
	try:
		# Check if there is coversation or not

		user = UserInfo.objects.get(user = request.user)
		other_user_obj = UserInfo.objects.get(id = username)
		thread_obj, is_created =  check_conversation(request.user, username)
		messages_ = None
		
		# This message object is used to mark all messages as read.
		message_object = Message.objects.filter(conversation_id=thread_obj).exclude(origin_user=user)
		message_object.update(read=True)
		##

		requested_user_info = UserInfo.objects.get(id=username)
		contact_thread  = Conversation.objects.filter((Q(user_1=user) & Q(user_2=other_user_obj)) |  (Q(user_2=user) & Q(user_1=other_user_obj)))
		contacts  = Conversation.objects.filter(Q(user_1=user) | Q(user_2=user))

		messages_all = Message.objects.filter(conversation_id__in = contacts).order_by('-timestamp').values('conversation_id')
		filtered_contacts = OrderedSet()

		# This does not include all the messages. Only include messages that had message
		for each_ in messages_all:
			filtered_contacts.add(str(each_['conversation_id']))

		# This will ensure that all the contatc that did not initiate message will be displayed
		for each_ in contacts:
			filtered_contacts.add(str(each_.id))


		# if contact_thread.count() > 0:
		# 	messages_ = Message.objects.filter(conversation_id=contact_thread[0]).order_by('timestamp')
		other_users = []

		for contact_ in filtered_contacts:
			contact = Conversation.objects.filter(id=contact_)[0]
			messages = Message.objects.filter(conversation_id=contact, read=False).exclude(origin_user=user)
			latest_message = Message.objects.filter(conversation_id=contact).order_by('-timestamp')

			# if latest_message.count() == 0:
			# 	latest_message = None

			if latest_message.count() > 0 or (str(contact_) == str(thread_obj.id) ):
				if contact.user_1.id != user.id:
					other_users.append({'id' : contact.user_1.id,
									'name' : contact.user_1.user.username.split('@')[0], 
									'username' : contact.user_1.user.username,
									'first_name' : contact.user_1.user.first_name if len(contact.user_1.user.first_name) > 0 else None,
									'last_name' : contact.user_1.user.last_name if len(contact.user_1.user.last_name) > 0 else None,
									'img': contact.user_1.profile_img,
									'unread': True if messages.count() > 0 else False,
									'latest_message': latest_message[0].message_text if latest_message else None,
									'latest_message_date' : str(latest_message[0].timestamp) if latest_message else None,
									})
				else:
					other_users.append({'id' : contact.user_2.id,
									'name' : contact.user_2.user.username.split('@')[0], 
									'username' : contact.user_2.user.username,
									'first_name' : contact.user_2.user.first_name if len(contact.user_2.user.first_name) > 0 else None,
									'last_name' : contact.user_2.user.last_name if len(contact.user_2.user.last_name) > 0 else None,
									'img': contact.user_2.profile_img,
									'unread': True if messages.count() > 0 else False,
									'latest_message': latest_message[0].message_text if latest_message else None,
									'latest_message_date' : str(latest_message[0].timestamp) if latest_message else None,
									})

		# If we do not have other user, then we just allow the user to start conversation
		# with the other user whose id is mentioned in the url. But the other person name or details
		# are not visible in messaging list.
		if len(other_users) == 0:
			contact_new = thread_obj.user_1 if thread_obj.user_1.id != user.id else thread_obj.user_2
			other_users.append({'id' : contact_new.id,
								'name' : contact_new.user.username.split('@')[0], 
								'username' : contact_new.user.username,
								'first_name' : contact_new.user.first_name if len(contact_new.user.first_name) > 0 else None,
								'last_name' : contact_new.user.last_name if len(contact_new.user.last_name) > 0 else None,
								'img': contact_new.profile_img,
								'unread':  False})
		context = {
		'id' : user.id,
		'allow_socket' : True,
		'other_users' : other_users,
		'error' : False,
		'base_url' : settings.BASE_AWS_IMG_URL,
		'other_user_pic' : requested_user_info.profile_img,
		
		'current_user_pic' : user.profile_img,
		'allow_chat' : True,
		'other_user_username' : requested_user_info.user.username.split('@')[0] if not len(requested_user_info.user.first_name) > 0 else requested_user_info.user.first_name ,
		'messages' : messages_,
		'current_user_obj' : user,
		'category' : product_choices.category,
		}
		
		return render(request, 'chat/chatthread.html', context)
	
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		raise Exception()


@login_required
def contacts(request):
	try : 
		user = UserInfo.objects.get(user = request.user)
		contacts  = Conversation.objects.filter(Q(user_1=user) | Q(user_2=user))
		other_users = []
		messages_all = Message.objects.filter(conversation_id__in = contacts).order_by('-timestamp').values('conversation_id')

		# These are filtered according to the latest message and now we only
		# have messages that started conversation with atleast one message
		filtered_contacts =  OrderedSet()
		for each_ in messages_all:
			filtered_contacts.add(str(each_['conversation_id']))
			
		for each_ in contacts:
			filtered_contacts.add(str(each_.id))
		
		for contact_ in filtered_contacts:
			
			contact = Conversation.objects.filter(id=contact_)[0]
			messages = Message.objects.filter(conversation_id=contact, read=False).exclude(origin_user=user)
			latest_message = Message.objects.filter(conversation_id=contact).order_by('-timestamp')

			# if latest_message.count() == 0:
			# 	latest_message = None

			if latest_message.count() > 0:
				if contact.user_1.id != user.id:
					other_users.append({'id' : contact.user_1.id,
									'name' : contact.user_1.user.username.split('@')[0], 
									'username' : contact.user_1.user.username,
									'first_name' : contact.user_1.user.first_name if len(contact.user_1.user.first_name) > 0 else None,
									'last_name' : contact.user_1.user.last_name if len(contact.user_1.user.last_name) > 0 else None,
									'img': contact.user_1.profile_img,
									'unread': True if messages.count() > 0 else False,
									'latest_message': latest_message[0].message_text if latest_message else None,
									'latest_message_date' : str(latest_message[0].timestamp) if latest_message else None
									})
				else:
					other_users.append({'id' : contact.user_2.id,
									'name' : contact.user_2.user.username.split('@')[0], 
									'username' : contact.user_2.user.username,
									'first_name' : contact.user_2.user.first_name if len(contact.user_2.user.first_name) > 0 else None,
									'last_name' : contact.user_2.user.last_name if len(contact.user_2.user.last_name) > 0 else None,
									'img': contact.user_2.profile_img,
									'unread': True if messages.count() > 0 else False,
									'latest_message': latest_message[0].message_text if latest_message else None,
									'latest_message_date' : str(latest_message[0].timestamp) if latest_message else None
									})

		context = {
		'id' : user.id,
		'allow_socket' : True,
		'other_users' : other_users,
		'error' : False,
		'base_url' : settings.BASE_AWS_IMG_URL,
		'category' : product_choices.category,
		'category' : product_choices.category,
		}
		
		
	except Exception as e:
		logging.getLogger("error_logger").error(str(e))
		context = {
			'allow_socket' : False,
			'other_users' : [],
			'error' : True,
			'category' : product_choices.category,
		}
	
	return render(request, 'chat/chatthread.html', context)


# This function is used to check if the two users are already connected or not.
# If users are not connected, then we create a new conversation id 
def check_conversation(user, other_user):
	return Conversation.objects.get_or_create(user, other_user)