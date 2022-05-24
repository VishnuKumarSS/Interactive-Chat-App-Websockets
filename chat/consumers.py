import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name'] # it updates the room_name in routing.py in our app.
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # we can use async_to_sync 
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
        # the json dumps converts the python object to a json string .





















# class ChatRoomConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
        
#         await self.channel_layer.group_add(
#             # here the channel_layer is from the channels module
#             self.room_group_name,
#             self.channel_name
#         )
        
#         await self.accept()
        
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'tester_message',
#                 'tester': 'Just the testing message',
#             }
#         )
        
#     async def tester_message(self, event):
#         tester = event['tester']
        
#         await self.send(text_data=json.dumps({
#             'tester':tester,
#         }))
     
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )