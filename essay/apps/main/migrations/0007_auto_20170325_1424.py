# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170325_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_essay',
            name='user_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='essay',
            name='due_time',
            field=models.DateField(default='2017-01-01'),
        ),
        migrations.AlterField(
            model_name='essay',
            name='title',
            field=models.CharField(default='no title', max_length=100),
        ),
    ]
