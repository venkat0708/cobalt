# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160408_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.Category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='resources_required',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
