# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_gameproduct'),
        ('purchase', '0004_auto_20170401_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserecord',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='games.Item'),
            preserve_default=False,
        ),
    ]
