# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='currency',
            field=models.CharField(blank=True, default='EUR', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='invested',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='position',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='underlying',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='valuation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
