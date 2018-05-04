from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone
from category.models import Category
from categorie.models import Categorie


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
    categorie = models.ForeignKey(Categorie, null=True)
    category = models.ForeignKey(Category, null=True)
    delivery_time = models.CharField(max_length=50)

    def get_delete_url(self):
        return reverse("post:delete-post", kwargs={"slug": self.slug})

class Comment(models.Model):
    post = models.ForeignKey('post.PostModel', related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    body = models.TextField()
    created_date = models.DateField(default=timezone.now)
    parent = models.ForeignKey("self", blank=True, null=True)
    is_parent = models.BooleanField(default=True)

    def __str__(self):
        return self.body

    def children(self):
        return Comment.objects.filter(parent=self)