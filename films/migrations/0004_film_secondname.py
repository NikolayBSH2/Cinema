# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 14:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20160414_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='secondname',
            field=models.CharField(default=datetime.datetime(2016, 4, 14, 14, 11, 33, 965500, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
