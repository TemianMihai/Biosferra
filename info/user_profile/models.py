from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid

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
    mesaj = models.CharField(max_length=1000)
    titlu = models.CharField(max_length=100, null=True)
    destinatar = models.ForeignKey(to=User, related_name='reportt',
                                   null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
