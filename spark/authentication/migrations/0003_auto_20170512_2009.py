# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-12 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170424_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'aluno', 'verbose_name_plural': 'alunos'},
        ),
    ]
