# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0015_auto_20171129_1451'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TypeEqm',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='type_of_eqm',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='type_of_eqm',
            new_name='type',
        ),
    ]
