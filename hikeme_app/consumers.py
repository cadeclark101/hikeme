import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer



class UserConsumer(WebsocketConsumer):
    def websocket_connect(self, event):
        self.user_id = self.scope["user"]
        self.user_group_name = "active_users"
        async_to_sync(self.channel_layer.group_add)(
            self.user_group_name, self.channel_name
        )
        self.accept() # call this last

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer_group.group_discard)(
            self.user_group_name, self.channel_name
        )

    def send_user(self, event):
        user = event["data"]
        self.send(json.dumps({"user": user}))

    def websocket_receive(self):
        pass