# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-11-15 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='qq',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]