# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-24 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190324_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='description',
            field=models.CharField(max_length=200, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043a \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
    ]