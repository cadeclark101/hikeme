from django.db import models
from django.conf import settings


class Trail(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    difficulty = models.IntegerField()


class Trail_Checkpoint(models.Model):
    trail = models.ForeignKey(
    Trail,
    on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    emergency_contact_number = models.IntegerField()
    address = models.TextField()
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    ) 

class CheckIn(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete = models.CASCADE
    )
    trail = models.OneToOneField(
        Trail,
        on_delete=models.CASCADE
    )
    trail_checkpoint = models.OneToOneField(
        Trail_Checkpoint,
        on_delete=models.CASCADE
    )
    datetime_of_checkin = models.DateTimeField()

class Hike(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    trail = models.OneToOneField(
        Trail,
        on_delete=models.CASCADE
    )
    checkins = models.ForeignKey(
        CheckIn,
        on_delete=models.CASCADE
    )
    completed = models.BooleanField()

class Status(models.Model):
    status = models.CharField(max_length=60)
    date_posted = models.DateTimeField()
    likes = models.IntegerField
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    

class Warning(models.Model):
    trail = models.ForeignKey(
    Trail,
    on_delete=models.CASCADE
    )
    trail_checkpoint = models.ManyToManyField(
    Trail_Checkpoint,
    )
    warning = models.CharField(max_length=100)
    warning_rating = models.IntegerField()
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

