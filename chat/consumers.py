import json
from channels.generic.websocket import WebsocketConsumer


class chatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!' 
        }))

    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print('Message: ', message)

        self.send(text_data=json.dumps({
            'type':'chat',
            'message': message
        }))