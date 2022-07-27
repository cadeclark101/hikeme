from tkinter import CASCADE
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    emergency_contact_number = models.IntegerField()
    address = models.TextField()
    departure = models.DateTimeField()
    eta = models.DateTimeField()

class Status(models.Model):
    person_status = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=100)
    datetime = models.DateTimeField()

class Trail(models.Model):
    person_trail = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    trail_name = models.CharField(max_length=100)
    trail_checkpoint = models.IntegerField()
    trail_length = models.IntegerField()

class Warning(models.Model):
    trail = models.ForeignKey(
    Trail,
    on_delete=models.CASCADE
    )
    warning = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    
class Authority(models.Model):
    last_known_location = models.OneToOneField(
        Trail,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    
