from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone
from category.models import Category
from categorie.models import Categorie
from lfcat.models import Products

# Create your models here.
CHOICES_UM = ((0, "Kg"), (1, "Buc"))
CHOICES_SEASON = ((0, "Primavara"), (1, "Vara"), (2, "Toamna"), (3, "Iarna"))


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

class PostModel(models.Model):
    author = models.ForeignKey(to=User, related_name='posts',
                               null=True, blank=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    image1 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    image2 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    image3 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    image4 = models.ImageField(upload_to = upload_location,
                              null=True, blank=True)
    price = models.IntegerField(default=0)
    season = models.IntegerField(choices=CHOICES_SEASON)
    um = models.IntegerField(choices=CHOICES_UM)
    product_type = models.ForeignKey(Products, null=True)
    approved = models.BooleanField(default=False)

    def get_delete_url(self):
        return reverse("post:delete-post", kwargs={"slug": self.slug})

    def get_comanda_url(self):
        return reverse("post:get-comanda", kwargs={"slug":self.slug})

    def get_finalizare_url(self):
        return reverse("post:get-finalizare", kwargs={"slug":self.slug})


class CosulMeu(models.Model):
    anunturi =  models.ForeignKey(to = PostModel, related_name='cos_comandaa',
                                null=True, blank=True)
    cumparator = models.ForeignKey(to=User, related_name='cos_cumparator',
                                   null=True, blank=True)
    vanzator = models.ForeignKey(to=User, related_name='cos_vanzator',
                                 null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

    def get_delete_cos_url(self):
        return reverse("post:delete-anunt-cos", kwargs={"slug": self.slug})

class Comanda(models.Model):
    comenzi = models.ForeignKey(to = PostModel, related_name='comanda',
                                null=True, blank=True)
    cumparator = models.ForeignKey(to=User, related_name='comanda_cumparator',
                                   null=True, blank=True)
    vanzator = models.ForeignKey(to=User, related_name='comanda_vanzator',
                                 null=True, blank=True)

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


class AdresaDeFacturare(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    nrdetelefon = models.CharField(max_length=10)
    adresa = models.CharField(max_length=100)
    judet = models.CharField(max_length=50)
    localitate = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=50)
    tva = models.BooleanField(default=True)
    posesor = models.ForeignKey(to=User, related_name='posesor',
                                 null=True, blank=True)
    creator = models.ForeignKey(to=User, related_name='detinator',
                                  null=True, blank=True)
    postcomanda = models.ForeignKey(to=PostModel, related_name='post_comanda',
                                    null=True, blank=True)
    nume2 = models.CharField(max_length=50, null=True)
    prenume2 = models.CharField(max_length=50, null=True)
    adresa2 = models.CharField(max_length=100, null=True)
    judet2 = models.CharField(max_length=50, null =True)
    localitate2 = models.CharField(max_length=50, null=True)
    codpostal2 = models.CharField(max_length=50,null=True)
    comentarii = models.CharField(max_length=1000, null=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

    def get_delete_comands_url(self):
        return reverse("post:delete-comanda", kwargs={"slug": self.slug})

    def get_comandap_url(self):
        return reverse("post:get-comandap", kwargs={"slug":self.slug})

    def get_comandat_url(self):
        return reverse("post:get-comandat", kwargs={"slug":self.slug})