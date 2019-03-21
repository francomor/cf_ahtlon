# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-10 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20180929_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='domicilio',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='es_socio',
            field=models.BooleanField(default=False),
        ),
    ]