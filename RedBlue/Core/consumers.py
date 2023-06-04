import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AuctionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'auction'
        self.room_group_name = 'room_auction'


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

    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     data = text_data_json['data']
    #     print(data)
    #     # Send message to room group
    #     await self.send(text_data=json.dumps(
    #        {
    #           'type': 'chat_message',
    #          'time': data['E']//1000,
    #         'price':float(data['c']),
    #        }))
    # Receive message from room group
    async def Send_winner_color(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'event': "Send_winner_color",
            'color': event['color'],
        }))
    async def Send_auction_start(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'event': "State_auction",
            'state': event['state'],
        }))



