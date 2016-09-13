# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='classroom',
        ),
        migrations.AddField(
            model_name='subject',
            name='classroom',
            field=models.ManyToManyField(to='journal.Classroom'),
        ),
    ]
