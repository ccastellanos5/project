# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170522_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
