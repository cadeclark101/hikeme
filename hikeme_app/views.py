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
        if request.user.is_authenticated:
            self.current_user = request.user
            self.current_person = get_object_or_404(Person, auth_user_id = self.current_user.id)

            return render(request=request, template_name="home.html", 
            context={"current_person":self.current_person, "current_trail":self.getCurrentUserTrail, "current_trail_checkpoint":self.getCurrentUserTrailCheckpoint, "all_trails":self.getAllTrails, "all_warnings":self.getWarnings, "all_check_ins":self.getAllCheckIns, "last_check_in":self.getLastUserCheckIn, "risk_counts":self.getWarningCounts, "next_checkpoint":self.getNextCheckPoint})
        else:
            return redirect("/accounts/login")

    def getCurrentUserTrail(self):
        current_trail = get_object_or_404(Trail, pk = self.current_person.current_trail_id)
        return current_trail

    def getCurrentUserTrailCheckpoint(self):
        current_trail_checkpoint = get_object_or_404(Trail_Checkpoint, pk = self.current_person.current_trail_checkpoint_id)
        return current_trail_checkpoint

    def getAllTrails(self):
        all_trails = Trail.objects.all()
        return all_trails

    def getNewsFeed(self):
        news_current_checkpoint = get_object_or_404(News, relevant_trail_checkpoint = self.current_person.current_trail_checkpoint_id)
        news_current_trail = get_object_or_404(News, relevant_trail = self.current_person.current_trail_id)
        return news_current_checkpoint, news_current_trail

    def getWarnings(self):
        all_warnings = Warning.objects.filter(person = self.current_person.id)
        return all_warnings

    def getWarningCounts(self):
        all_warnings = self.getWarnings()
        high_risk_count = sum(1 for warning in all_warnings if warning.warning_rating in range(4,6))
        medium_risk_count = sum(1 for warning in all_warnings if warning.warning_rating in range(3,4))
        low_risk_count = sum(1 for warning in all_warnings if warning.warning_rating in range(1,3))
        return high_risk_count, medium_risk_count, low_risk_count

    def getAllCheckIns(self):
        all_check_ins = CheckIn.objects.filter(person = self.current_person.id)
        return all_check_ins

    def getLastUserCheckIn(self):
        last_check_in = CheckIn.objects.filter(person = self.current_person.id).last()
        return last_check_in

    def getNextCheckPoint(self):
        all_checkpoints_for_trail = Trail_Checkpoint.objects.filter(trail = self.current_person.current_trail)
        for i in all_checkpoints_for_trail:
            if (self.current_person.current_trail_checkpoint.id + 1) == i.id:
                next_checkpoint = Trail_Checkpoint.objects.filter(id = (self.current_person.current_trail_checkpoint.id + 1))
                return next_checkpoint[0]

    def getRelevantStatuses(self):
        pass



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
