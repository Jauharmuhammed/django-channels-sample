from django.urls import re_path
from chat.consumers import chatConsumer


websocket_urlpatterns = [
    re_path(r'ws/socket-server', chatConsumer.as_asgi()),
]

