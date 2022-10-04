from django.conf.urls import url

from chat import consumers

websocket_urlpatterns = [
    url(r"^ws$", consumers.ChatConsumer.as_asgi()),
]
