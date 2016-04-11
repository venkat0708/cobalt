# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_associate'),
        ('workflow', '0002_auto_20160409_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='services',
            field=models.ManyToManyField(to='services.Service'),
        ),
    ]