# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-21 13:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 21, 13, 44, 40, 91610, tzinfo=utc)),
        ),
    ]
