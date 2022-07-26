from django.shortcuts import  render, redirect
from django.urls import is_valid_path
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse

def home(request):
    return redirect("/")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Error when registering")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})