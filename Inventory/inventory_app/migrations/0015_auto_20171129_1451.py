# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0014_auto_20171128_1130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='TypeEqm',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='type',
            new_name='type_of_eqm',
        ),
        migrations.RenameField(
            model_name='typeeqm',
            old_name='type',
            new_name='type_of_eqm',
        ),
    ]
