# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='buddy',
        ),
        migrations.AddField(
            model_name='trip',
            name='planner',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='travelers',
            field=models.ManyToManyField(related_name='traveling', to='travelbuddy.User'),
        ),
    ]