# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0009_auto_20171123_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='name',
            new_name='user',
        ),
    ]