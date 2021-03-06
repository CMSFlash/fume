# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.FilePathField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='thumbnail',
            field=models.FilePathField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('game', 'platform')]),
        ),
    ]
