#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Document, Editor


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'page',
                    'author',
                    'allowed',
                    'added',
                    )

    search_fields = ('title', 'added')
    ordering = ('title', 'added')
    list_filter = ('title', 'added')


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'page',
                    'author',
                    'allowed',
                    'added',
                    )

    search_fields = ('title', 'added')
    ordering = ('title', 'added')
    list_filter = ('title', 'added')
