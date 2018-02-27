from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
import uuid
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save


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
    price = models.CharField(max_length=15)
    delivery_time = models.CharField(max_length=50)


def get_absolute_url(self):
         return reverse("post:post-get", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = PostModel.objects.filter(slug=slug).ordered_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = PostModel.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=PostModel)