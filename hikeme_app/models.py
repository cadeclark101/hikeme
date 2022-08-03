from tkinter import CASCADE
from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=100)

class Trail(models.Model):
    name = models.CharField(max_length=100)

class Trail_Checkpoint(models.Model):
    trail = models.ForeignKey(
    Trail,
    on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100) 
    
class Warning(models.Model):
    trail_checkpoint = models.ForeignKey(
    Trail_Checkpoint,
    on_delete=models.CASCADE
    )
    warning = models.CharField(max_length=100)
    warning_rating = models.IntegerField()

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    emergency_contact_number = models.IntegerField()
    address = models.TextField()
    current_status = models.OneToOneField(
        Status,
        on_delete=models.CASCADE
    )
    current_trail_checkpoint = models.OneToOneField(
        Trail_Checkpoint,
        on_delete=models.CASCADE
    )