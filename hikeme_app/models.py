from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    class Meta:
        db_table="Login"
