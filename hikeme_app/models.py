from django.db import models
from django.conf import settings


class Status(models.Model):
    status = models.CharField(max_length=60)
    date_posted = models.DateTimeField()
    likes = models.IntegerField

class Trail(models.Model):
    name = models.CharField(max_length=100)

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
    statuses = models.ManyToManyField(
        Status,
        blank=True,
        null=True
    )
    current_trail = models.OneToOneField(
        Trail,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    current_trail_checkpoint = models.OneToOneField(
        Trail_Checkpoint,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class CheckIn(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete = models.CASCADE
    )
    trail_checkpoint = models.OneToOneField(
        Trail_Checkpoint,
        on_delete=models.CASCADE
    )
    datetime_of_checkin = models.DateTimeField()
    

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

class News(models.Model):
    text = models.CharField(max_length=1000)
    relevant_trail_checkpoint = models.ManyToManyField(
        Trail_Checkpoint
    )
    relevant_trail  = models.ManyToManyField(
        Trail
    )

class Leaderboard(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    trail = models.ForeignKey(
    Trail,
    on_delete=models.CASCADE
    )
    time_taken = models.IntegerField()
