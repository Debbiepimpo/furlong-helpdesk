# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-01-08 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0005_auto_20200108_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='hour',
            name='name',
            field=models.TextField(default='Test', max_length=500),
            preserve_default=False,
        ),
    ]
