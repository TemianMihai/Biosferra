from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
import uuid

def upload_location(instance, filename):
    return "%s/%s" % (instance.product1, filename)

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(to=User, related_name='sent_messages',
                               null=True, blank=True)
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=100, null=True)
    receiver = models.ForeignKey(to=User, related_name='received_messages',
                                 null=True, blank=True)
    created_date = models.DateField(default=timezone.now)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

    def get_mesajt_url(self):
        return reverse("mesaj:get-mesajt", kwargs={"slug":self.slug})

class Report(models.Model):
    author = models.ForeignKey(to=User, related_name='sent_reports',
                               null=True, blank=True)
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=100, null=True)
    receiver = models.ForeignKey(to=User, related_name='received_reports',
                                 null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

class Favourite(models.Model):
    author = models.ForeignKey(to=User, related_name='favourites_by',
                               null=True, blank=True)
    is_favourite = models.BooleanField(default=False)
    receiver = models.ForeignKey(to=User, related_name='favourites',
                                 null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="profile")
    product1 = models.CharField(max_length=30)
    product2 = models.CharField(max_length=30)
    product3 = models.CharField(max_length=30)
    product4 = models.CharField(max_length=30)
    product5 = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    profile_image = models.ImageField(upload_to=upload_location,
                                      null=True, blank=True)
    cover_image = models.ImageField(upload_to=upload_location,
                                    null=True, blank=True)

    def get_profilf_url(self):
        return reverse("profil:get-profilt")