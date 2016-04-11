# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20160409_2013'),
        ('services', '0006_service_associate'),
        ('workflow', '0003_event_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceMaster',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.BaseEntity')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
            bases=('people.baseentity',),
        ),
        migrations.AlterField(
            model_name='event',
            name='services',
            field=models.ManyToManyField(to='workflow.ServiceMaster'),
        ),
    ]
