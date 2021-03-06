# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170625_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='exposure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='realized_profit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='volume',
            field=models.FloatField(blank=True, help_text='Usually integer number of units (+ if we bought, - if we sold)', null=True),
        ),
    ]
