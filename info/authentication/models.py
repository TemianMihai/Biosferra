from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phonenumber = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length= 20)
    adress = models.CharField(max_length= 20, null= True)
    state = models.CharField(max_length= 20, null= True)