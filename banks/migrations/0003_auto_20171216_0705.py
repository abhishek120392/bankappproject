# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_auto_20171216_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=49),
        ),
    ]
