# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '__first__'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='actividades',
            field=models.ManyToManyField(blank=True, to='actividades.Actividad'),
        ),
    ]