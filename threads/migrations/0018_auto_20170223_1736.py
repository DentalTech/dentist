# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 17:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0017_auto_20170223_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 17, 36, 13, 31596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 17, 36, 13, 30224, tzinfo=utc)),
        ),
    ]