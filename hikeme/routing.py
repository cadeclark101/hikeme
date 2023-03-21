from django.urls import path
from hikeme_app.consumers import UserConsumer

ws_urlpatterns = [
    path('', UserConsumer.as_asgi())
]