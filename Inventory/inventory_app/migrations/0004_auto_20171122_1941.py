# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0003_auto_20171122_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='user',
            new_name='Сотрудник',
        ),
    ]