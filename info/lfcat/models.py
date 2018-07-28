from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lfcategory(models.Model):
    name = models.CharField(null=True, max_length=10)
    def __unicode__(self):
        return self.name

class Legfruccategory(models.Model):
    name = models.CharField(null = True, max_length=20)
    def __unicode__(self):
        return self.name