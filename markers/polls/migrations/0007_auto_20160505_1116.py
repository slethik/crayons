# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160505_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='response',
            new_name='poll_choice',
        ),
    ]
