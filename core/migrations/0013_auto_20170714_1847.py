# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170626_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trade',
            options={'ordering': ['-trade_date']},
        ),
        migrations.RemoveField(
            model_name='trade',
            name='underlying',
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.FloatField(blank=True, help_text='The price of the unit (value = volume * price + transaction cost)', null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='value',
            field=models.FloatField(blank=True, help_text='How much money did we pay in this trade, including costs (+ if we payed, - if we got the money)', null=True),
        ),
    ]
