# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20170220_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 9, 46, 7, 454698, tzinfo=utc)),
        ),
    ]