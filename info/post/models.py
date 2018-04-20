from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
import uuid
from category.models import Category



# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

class PostModel(models.Model):
    author = models.ForeignKey(to=User, related_name='posts',
                               null=True, blank=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    cantity = models.CharField(max_length=100)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    image1 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    image2 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    image3 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    image4 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    price = models.CharField(max_length=15)
    category = models.ForeignKey(Category, null=True)
    delivery_time = models.CharField(max_length=50)

    def get_delete_url(self):
        return reverse("post:delete-post", kwargs={"slug": self.slug})
