# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 20:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0006_auto_20160510_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to=settings.AUTH_USER_MODEL),
        ),
    ]