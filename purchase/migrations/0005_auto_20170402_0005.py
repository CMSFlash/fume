# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_auto_20170401_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserecord',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_records', to='games.Item'),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_records', to='member.Member'),
        ),
    ]
