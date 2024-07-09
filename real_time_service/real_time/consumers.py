import json
from channels.generic.websocket import AsyncWebsocketConsumer
import pika

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            await self.accept()
            self.channel_name = f"user_{self.user.id}"
            self.channel_layer.group_add(self.channel_name, self.channel_name)

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(self.channel_name, self.channel_name)

    async def receive(self, text_data):
        pass

    async def notify(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))

    @classmethod
    def send_to_users(cls, users, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='notifications')
        for user in users:
            channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps({'user': user, 'message': message}))
        connection.close()
