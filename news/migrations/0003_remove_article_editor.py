# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-08 06:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190307_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
    ]