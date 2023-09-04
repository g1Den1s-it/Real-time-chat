import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.auth import get_user
from django.shortcuts import get_object_or_404

from chat.models import Chat, Message
from user.models import User
from django.urls import reverse


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = 'chats'
        self.user_data = None

    async def connect(self):
        user = self.scope['user']

        if user.is_anonymous:
            await self.accept()
            await self.send(json.dumps({'redirect_url': reverse('users:sign-in')}))
            await self.close()
        else:
            self.user_data = await get_user(self.scope)
            await self.channel_layer.group_add(self.room_name, self.channel_name)
            await self.accept()
            await self.send(text_data=json.dumps(await self.get_user_chats()))

    async def disconnect(self, code):
        print(f"disconected: {code}")
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        if 'chat' in text_data_json:
            await self.send(text_data=json.dumps(await self.get_message_data(text_data_json['chat'])))
            await self.channel_layer.group_discard(self.room_name, self.channel_name)

            self.room_name = text_data_json['chat']

            await self.channel_layer.group_add(self.room_name, self.channel_name)

        elif 'new_message' in text_data_json:
            message = await self.save_message(
                text_data_json['chat_name'],
                text_data_json['new_message'])

            print(f'room_name: {self.room_name}')
            await self.channel_layer.group_send(
                self.room_name,
                {
                    "type": "chat_message", "message": message
                }
            )

    async def chat_message(self, event):
        message = event['message']
        print('called this def')
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

    @database_sync_to_async
    def get_message_data(self, custom_id):
        message = Message.objects.filter(chat__custom_id=custom_id)
        message_list = {
            'list_message': [
                {
                    'id': mes.id,
                    'text': mes.text,
                    'owner': mes.owner.username,
                    'date': mes.date.strftime('%H:%M'),
                    'owner_image': mes.owner.image.url,
                } for mes in message
            ]
        }
        return message_list

    @database_sync_to_async
    def get_user_chats(self):
        chats = Chat.objects.filter(user=self.user_data)
        user = get_object_or_404(User, tag=self.user_data)
        chats_list = {
            "list_chat": [
                {
                    'id': chat.id,
                    'custom_id': chat.custom_id,
                    'name': chat.name,
                    'owner': chat.owner.username if chat.owner else None,
                    'user': [user.username for user in chat.user.all()],
                    'create_date': chat.create_date.strftime('%Y-%m-%d %H:%M:%S')
                }
                for chat in chats
            ],
            'user': {
                'id': user.id,
                'username': user.username,
                'image': user.image.url,
            }
        }
        return chats_list

    @database_sync_to_async
    def save_message(self, chat_name, message):
        chat = get_object_or_404(Chat, custom_id=chat_name)
        user = get_object_or_404(User, tag=self.user_data)
        message = Message.objects.create(
            text=message,
            owner=user,
            chat=chat
        )
        message.save()
        message_object = {
            'id': message.id,
            'text': message.text,
            'owner': message.owner.username,
            'date': message.date.strftime('%H:%M'),
            'owner_image': message.owner.image.url,
        }
        return message_object
