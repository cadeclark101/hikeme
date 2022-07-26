from django.shortcuts import render
from .models import Login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, DJANGO!")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        encryptedpassword = make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword = check_password(request.POST['password'], encryptedpassword)
        print(checkpassword)
        data = Login(username=username, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')

    else: 
        return render(request, 'home.html')
