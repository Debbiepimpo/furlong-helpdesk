# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-01-07 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0003_auto_20200107_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='requested_date',
            field=models.DateTimeField(),
        ),
    ]