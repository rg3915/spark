# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-01 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='photo',
            field=models.URLField(blank=True, null=True, verbose_name='foto'),
        ),
    ]