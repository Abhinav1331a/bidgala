# Standard library imports
from django.contrib.auth.models import User
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
import asyncio
import json
import re

# Related third party imports

# Local application/library specific imports
from accounts.models import UserInfo
from .models import Conversation
from .models import Message


class ChatConsumer(AsyncConsumer):
	async def websocket_connect(self, event):

		try:
   			if self.scope['user'].is_anonymous:
   				await self.close()
   			other_user = self.scope['url_route']['kwargs']['username']
   			thread_obj, is_created = await self.get_conversation(other_user)
   			chat_room = f"thread_{thread_obj.id}"
   			self.conversation_id = thread_obj.id
   			self.chat_room = chat_room
   			self.current_user_id = await self.get_currentUserID()
   			await self.channel_layer.group_add(
   				chat_room,
				self.channel_name
				)
   			await self.send({
				"type" : "websocket.accept"
				})
		except Exception as e:
			self.send({
            "type": "websocket.disconnect",
        })

	async def websocket_receive(self, event):

		front_text = event.get('text', None)
		if front_text is not None:
			user = self.scope['user']
			loaded_dict_data = json.loads(front_text)
			if loaded_dict_data.get('type') == 'ack':
				ack_user_id = loaded_dict_data.get('user')
				if (user.is_authenticated) and (self.scope['url_route']['kwargs']['username'] != ack_user_id):
					await self.ack_message(ack_user_id, loaded_dict_data.get('msg_ack_id'))
				
			else:
				include_contact_info = False
				msg = loaded_dict_data.get('message')
				if (user.is_authenticated) and (self.scope['url_route']['kwargs']['username'] != loaded_dict_data.get('user')):
					try:
						if len(loaded_dict_data.get('message').strip()) > 0:
							if (len(re.findall('\S+@\S+', loaded_dict_data.get('message').strip())) > 0) or \
								(len(re.findall('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', loaded_dict_data.get('message').strip()) ) > 0):
								msg_obj, created, include_contact_info = None, False, True
							else:
								msg_obj, created = await self.store_message(self.conversation_id, loaded_dict_data.get('user'), loaded_dict_data.get('message').strip())
						
					except Exception as e:
						self.send({
	            			"type": "websocket.disconnect",
	    			    })

					if include_contact_info:
						myResponse = {
							'message' : 'Contact information is restricted',
							'id' : str(self.current_user_id),
							'timestamp' : str(msg_obj.timestamp),
							'echo_to_sender' : loaded_dict_data.get('user'),
						}

					else:	
						myResponse = {
							'message' : msg,
							'send_ack_id' : msg_obj.id,
							'id' : str(self.current_user_id),
							'timestamp' : str(msg_obj.timestamp),
							'echo_to_sender' : loaded_dict_data.get('user'),
						}

					await self.channel_layer.group_send(
						self.chat_room,
						{
							"type" : "chat_message",
							"text" : json.dumps(myResponse)
						}
					)
			

	# This is custom method
	async def chat_message(self, event):
		await self.send({
			"type" : "websocket.send",
			"text" : event['text']
			})


	async def websocket_disconnect(self, event):
		await self.channel_layer.group_discard(
            self.chat_room,
            self.channel_name
        )
		raise StopConsumer()

	@database_sync_to_async
	def get_conversation(self, other_user):
		user = self.scope['user']
		return Conversation.objects.get_or_create(user, other_user)

	@database_sync_to_async
	def get_currentUserID(self):
		user = self.scope['user']
		try:
			return UserInfo.objects.get(user = user).id
		except Exception as e:
			return None

	@database_sync_to_async
	def store_message(self, conversation_id, message_from, message):
		return Message.objects.store(conversation_id, message_from, message)

	@database_sync_to_async
	def ack_message(self, ack_user, message_id):
		return Message.objects.ack_message(ack_user, message_id)
		
		
 

class Notification(AsyncConsumer):
	async def websocket_connect(self, event):

		try:
   			if self.scope['user'].is_anonymous:
   				await self.close()
   			
   			chat_room = f"thread_{self.scope['user'].id}"
   			
   			self.chat_room = chat_room
   			await self.channel_layer.group_add(
   				chat_room,
				self.channel_name
				)
   			await self.send({
				"type" : "websocket.accept"
				})
		except Exception as e:
			self.send({
            "type": "websocket.disconnect",
        })

	async def websocket_receive(self, event):
		
		front_text = event.get('text', None)
		if front_text is not None:
			loaded_dict_data = json.loads(front_text)			
			user_to_notify = await self.get_OtherUserID(loaded_dict_data.get('thread_id'))
			user = self.scope['user']
			
			if (user.is_authenticated):
				
				myResponse = {
					
					'id' : str(await self.get_currentUserID()),
				}

				await self.channel_layer.group_send(
					f"thread_{user_to_notify}",
					{
						"type" : "notify",
						"text" : json.dumps(myResponse)
					}
				)

	async def websocket_disconnect(self, event):
		if self.chat_room and self.channel_name:
			await self.channel_layer.group_discard(
	        self.chat_room,
	        self.channel_name
	    	)
			raise StopConsumer()
		else:
			None

	@database_sync_to_async
	def get_currentUserID(self):
		user = self.scope['user']
		try:
			return UserInfo.objects.get(user = user).id
		except Exception as e:
			return None

	@database_sync_to_async
	def get_OtherUserID(self, id):
		try:
			return UserInfo.objects.get(id = id).user.id
		except Exception as e:
			return None

	# This is custom method
	async def notify(self, event):
		await self.send({
			"type" : "websocket.send",
			"text" : event['text']
			})

