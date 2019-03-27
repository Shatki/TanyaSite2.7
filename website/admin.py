#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Menu, Section, MailSet


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu',
                    'name',
                    'page',
                    'url',
                    )

    search_fields = ('name',)
    ordering = ('menu',)


@admin.register(MailSet)
class MailSetAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'default',
                    'email_host',
                    'email_host_port',
                    'email_host_user',
                    'email_host_password',
                    'email_use_tls',
                    'email_use_ssl',
                    )

    ordering = ('name',)

# Register your models here.
# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
#    fields = ('name',)
#    search_fields = ('name',)
#    list_display = ('name',)
