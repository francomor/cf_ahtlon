# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-21 01:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0003_auto_20181110_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='imagen',
        ),
    ]
