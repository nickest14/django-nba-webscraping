# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-15 02:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba_news', '0005_auto_20170914_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='text',
            new_name='content',
        ),
    ]
