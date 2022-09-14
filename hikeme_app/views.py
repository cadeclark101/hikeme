from django.shortcuts import  render, redirect
from django.shortcuts import get_object_or_404

from .forms import NewUserForm
from django.views import View
from .models import *

from django.contrib.auth import login
from django.contrib import messages

from django.http import HttpResponse

class Home(View):
    def get(self, request):
        self.current_user = request.user
        self.current_person = get_object_or_404(Person, auth_user_id = self.current_user.id)

        return render(request=request, template_name="home.html", 
        context={"current_person":self.current_person, "current_trail":self.getCurrentUserTrail(), "current_trail_checkpoint":self.getCurrentUserTrailCheckpoint(), "all_trails":self.getAllTrails()})

    def getCurrentUserTrail(self):
        current_trail = get_object_or_404(Trail, pk = self.current_person.current_trail_id)
        return current_trail

    def getCurrentUserTrailCheckpoint(self):
        current_trail_checkpoint = get_object_or_404(Trail_Checkpoints, pk = self.current_person.current_trail_checkpoint_id)
        return current_trail_checkpoint

    def getAllTrails(self):
        all_trails = Trail.objects.all()
        return all_trails



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
    return render (request=request, template_name="registration/register.html", context={"register_form":form,})
