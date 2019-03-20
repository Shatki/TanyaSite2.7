# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('pdf', '*.pdf \u0444\u0430\u0439\u043b Adobe Reader'), ('ppt', '*.ppt \u0444\u0430\u0439\u043b \u043f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u0438 MS PowerPoint 97/2003'), ('pptx', '*.pptx \u0444\u0430\u0439\u043b \u043f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u0438 MS PowerPoint'), ('doc', '*.doc \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b MS Word 97/2003'), ('docx', '*.docx \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b MS Word'), ('xls', '*.xls \u0444\u0430\u0439\u043b \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0445 \u0442\u0430\u0431\u043b\u0438\u0446 MS Excel 97/2003'), ('xlsx', '*.xlsx \u0444\u0430\u0439\u043b \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0445 \u0442\u0430\u0431\u043b\u0438\u0446 MS Excel'), ('unknown', '\u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0439 \u0442\u0438\u043f \u0444\u0430\u0439\u043b\u0430')], default='pdf', max_length=7, verbose_name='\u0442\u0438\u043f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430'),
        ),
    ]
