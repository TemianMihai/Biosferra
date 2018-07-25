from __future__ import unicode_literals

from django.db import models

CHOICES_TYPE = ((0, "Legume"), (1, "Fructe"))

class Products(models.Model):
    name = models.CharField(null=True, max_length=20)
    type = models.IntegerField(choices=CHOICES_TYPE)
    def __unicode__(self):
        return self.name