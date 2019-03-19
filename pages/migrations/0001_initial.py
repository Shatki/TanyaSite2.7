# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-19 05:05
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='\u0432\u0440\u0435\u043c\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('doc', models.FileField(upload_to=b'documents/', verbose_name='\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442')),
                ('preview', models.ImageField(blank=True, default=None, upload_to=b'miniatures/', verbose_name='\u043c\u0438\u043d\u0438\u0430\u0442\u044e\u0440\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
                ('allowed', models.BooleanField(default=False, verbose_name='\u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044e')),
                ('type', models.CharField(choices=[(b'pdf', b'*.pdf \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb Adobe Reader'), (b'ppt', b'*.ppt \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 MS PowerPoint 97/2003'), (b'pptx', b'*.pptx \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 MS PowerPoint'), (b'doc', b'*.doc \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb MS Word 97/2003'), (b'docx', b'*.docx \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb MS Word'), (b'xls', b'*.xls \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x8d\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86 MS Excel 97/2003'), (b'xlsx', b'*.xlsx \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x8d\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86 MS Excel'), (b'unknown', b'\xd0\xbd\xd0\xb5\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb8\xd0\xbf \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb\xd0\xb0')], default=b'pdf', max_length=7, verbose_name=b'\xd1\x82\xd0\xb8\xd0\xbf \xd0\xb4\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u0442\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u043b/\u0430\u0432\u0442\u043e\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Menu', verbose_name='\u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
            ],
            options={
                'db_table': 'documents',
                'verbose_name': '\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='\u0432\u0440\u0435\u043c\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('text', ckeditor.fields.RichTextField(verbose_name='\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442')),
                ('allowed', models.BooleanField(default=False, verbose_name='\u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044e')),
                ('header', models.FileField(null=True, upload_to=b'headers/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0432 \u0448\u0430\u043f\u043a\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u0442\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u043b/\u0430\u0432\u0442\u043e\u0440 \u0442\u0435\u043a\u0441\u0442\u0430')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Menu', verbose_name='\u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
            ],
            options={
                'db_table': 'editors',
                'verbose_name': '\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
    ]