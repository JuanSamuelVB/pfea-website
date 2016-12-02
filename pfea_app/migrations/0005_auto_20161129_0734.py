# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfea_app', '0004_auto_20161117_0229'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SolicitudDeVoluntario',
        ),
        migrations.AddField(
            model_name='voluntario',
            name='Solicitud_aceptada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voluntario',
            name='Horas_hechas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]