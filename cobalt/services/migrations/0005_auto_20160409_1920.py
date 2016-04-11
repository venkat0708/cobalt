# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_equipment_repair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='resources_required',
        ),
        migrations.AddField(
            model_name='service',
            name='resources_required',
            field=models.ManyToManyField(to='services.Equipment'),
        ),
    ]