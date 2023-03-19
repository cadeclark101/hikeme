"""
ASGI config for hikeme project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
from channels.routing import ProtocolTypeRouter, URLRouter
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hikeme.settings')

asgi_application = get_asgi_application() 

import hikeme_app.routing


application = ProtocolTypeRouter({
            "http": asgi_application,
            "websocket": URLRouter(hikeme_app.routing.websocket_urlpatterns) 
                       })
