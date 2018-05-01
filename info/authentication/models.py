from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phonenumber = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    adress = models.CharField(max_length= 50, null= True)
    state = models.CharField(max_length= 20, null= True)


class Account2(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phonenumber = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    adress = models.CharField(max_length= 50, null= True)
    state = models.CharField(max_length= 20, null= True)
    file1 = models.FileField(upload_to = upload_location,
                              null=True, blank=True)
    file2 = models.FileField(upload_to = upload_location,
                              null=True, blank=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1, null= True)
