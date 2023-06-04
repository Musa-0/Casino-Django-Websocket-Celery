from django.urls import re_path

from Account import consumers_for_user
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/connection/', consumers.AuctionConsumer.as_asgi()),
    re_path(r'ws/notification_connection/', consumers_for_user.NotificationConsumer.as_asgi()),

]