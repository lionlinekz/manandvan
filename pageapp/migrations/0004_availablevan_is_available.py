# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageapp', '0003_availablevan'),
    ]

    operations = [
        migrations.AddField(
            model_name='availablevan',
            name='is_available',
            field=models.IntegerField(default=0),
        ),
    ]
