# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0005_auto_20160729_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='modified',
        ),
        migrations.AddField(
            model_name='show',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]