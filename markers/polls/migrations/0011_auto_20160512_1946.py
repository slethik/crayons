# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 19:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160512_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='language',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='style',
        ),
        migrations.AlterField(
            model_name='pollresponse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PollResponse', to=settings.AUTH_USER_MODEL),
        ),
    ]
