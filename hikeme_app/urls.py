from django.urls import path
from hikeme_app import views

urlpatterns = [
    path("", views.home, name="home"),
]