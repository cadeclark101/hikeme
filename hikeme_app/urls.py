from django.urls import path
from hikeme_app import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from hikeme_app.views import Home

urlpatterns = [
    path('', views.Home.as_view()),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register_request, name="register"),
]