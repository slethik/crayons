# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0005_auto_20160510_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='phone_key',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='voter',
            name='phone_key_generated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
