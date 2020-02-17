# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-01-07 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
        ('hours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hourcomment',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='hourupvote',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='hourupvote',
            name='user',
        ),
        migrations.RenameField(
            model_name='hour',
            old_name='description',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='hour',
            old_name='totalHours',
            new_name='requested_hours',
        ),
        migrations.RemoveField(
            model_name='hour',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hour',
            name='purchases',
        ),
        migrations.AddField(
            model_name='hour',
            name='date',
            field=models.DateField(default='2020-01-06'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hour',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hour',
            name='requested_date',
            field=models.DateField(default='2020-01-06'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hour',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
        migrations.DeleteModel(
            name='HourComment',
        ),
        migrations.DeleteModel(
            name='HourUpvote',
        ),
    ]