from django.urls import path
from hikeme_app.consumers import PracticeConsumer

ws_urlpatterns = [
    path('', PracticeConsumer.as_asgi())
]