# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0010_auto_20171123_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='user',
            field=models.CharField(max_length=300, verbose_name='Сотрудник:'),
        ),
    ]
