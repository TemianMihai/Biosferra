# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-12 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account2',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]