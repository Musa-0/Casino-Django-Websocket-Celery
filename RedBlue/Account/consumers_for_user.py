import asyncio
import json

import redis
from channels.generic.websocket import AsyncWebsocketConsumer

from Core.service import make_stavka


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            self.room_name = self.scope["user"].id
            self.room_group_name = f'user_{self.room_name}'

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name)

    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    async def receive(self, text_data):
        if str(self.redis_client.get("access_for_make_stavka"))[2:-1]=="on":
            data_json = json.loads(text_data)
            user = self.scope["user"]
            data_json["user"] = user
            await make_stavka(data_json)
        else:
            print(str(self.redis_client.get("access_for_make_stavka"))[2:-1])





    async def Send_notification(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'event': "Send_notification",
            'message': event['message'],
        }))
