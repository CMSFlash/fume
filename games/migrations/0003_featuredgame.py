# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20170412_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
    ]
