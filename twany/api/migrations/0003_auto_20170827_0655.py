# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20170826_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_modified',
            field=models.DateTimeField(),
        ),
    ]