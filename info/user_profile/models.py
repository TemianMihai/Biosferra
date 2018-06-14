from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid

def upload_location(instance, filename):
    return "%s/%s" % (instance.produs1, filename)

# Create your models here.
class Mesaje(models.Model):
    autor = models.ForeignKey(to=User, related_name='mesaje',
                              null=True, blank=True)
    mesaj = models.CharField(max_length=1000)
    titlu = models.CharField(max_length=100, null=True)
    destinatar = models.ForeignKey(to=User, related_name='mesajee',
                                   null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

class Report(models.Model):
    autor = models.ForeignKey(to=User, related_name='report',
                              null=True, blank=True)
    mesajj = models.CharField(max_length=1000)
    titluu = models.CharField(max_length=100, null=True)
    destinatar = models.ForeignKey(to=User, related_name='reportt',
                                   null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

class Favorit(models.Model):
    alegator = models.ForeignKey(to=User, related_name='favorit',
                                 null=True, blank=True)
    favorite = models.BooleanField(default=False)
    ales = models.ForeignKey(to=User, related_name='favoritt',
                             null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

class Profile(models.Model):
    userul = models.ForeignKey(to = User, related_name='profile',
                               null=True, blank = True)
    produs1 = models.CharField(max_length=30)
    produs2 = models.CharField(max_length=30)
    produs3 = models.CharField(max_length=30)
    produs4 = models.CharField(max_length=30)
    produs5 = models.CharField(max_length=30)
    descriere = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_location,
                               null=True, blank=True)