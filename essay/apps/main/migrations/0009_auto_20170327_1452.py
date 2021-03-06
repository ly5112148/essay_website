# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 14:52
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='error_list',
            new_name='chart1',
        ),
        migrations.AddField(
            model_name='report',
            name='chart2',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='detail',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='error',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
    ]
