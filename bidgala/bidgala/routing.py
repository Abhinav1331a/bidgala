from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.conf.urls import url


from chat.consumers import ChatConsumer
from chat.consumers import Notification

application = ProtocolTypeRouter({
		'websocket' : AllowedHostsOriginValidator(
				AuthMiddlewareStack(
						URLRouter(
								[
									url(r"^ws/(?P<username>[\w.@+-]+)/$", ChatConsumer),
									url("notify/", Notification),
								]
							)
					)
			)
	})