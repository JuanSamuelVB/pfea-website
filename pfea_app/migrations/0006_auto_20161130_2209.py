# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfea_app', '0005_auto_20161129_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventariodeherramientas',
            name='Responsable2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventariodeherramientas',
            name='Responsable1',
            field=models.CharField(default='responsable', max_length=200),
            preserve_default=False,
        ),
    ]
