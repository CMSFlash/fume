# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='paymentMethod',
        ),
    ]