#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from romanovatatiana.settings import MENU_CHOICES, MENU_DEFAULT
from romanovatatiana.settings import PAGE_TYPES, NULL_PAGE
from django.core.mail.backends.smtp import EmailBackend


# Create your models here.
class Menu(models.Model):
    class Meta:
        verbose_name = u'страница меню'
        verbose_name_plural = u'страницы меню'
        db_table = u'menus'

    name = models.CharField(max_length=50, verbose_name=u'наименование страницы меню(отображается в навигации)')
    title = models.CharField(max_length=100, verbose_name=u'Основное наименование заголовка страницы меню')
    description = models.CharField(max_length=200, default=None, null=True, blank=True,
                                   verbose_name=u'дополнительное название заголовка страницы меню')
    menu = models.CharField(verbose_name=u"корневое меню", default=MENU_DEFAULT,
                            max_length=20, blank=False, choices=MENU_CHOICES)
    url = models.CharField(max_length=200, verbose_name=u"гиперссылка на страницу")

    page = models.CharField(verbose_name=u'тип страницы', default=NULL_PAGE, choices=PAGE_TYPES, max_length=20,
                            blank=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def get_type(self):
        return self.menu

    def get_url(self):
        if self.url[0] == u"#":
            return u"%s/%s" % (self.menu, self.url)
        return u"%s/%s/" % (self.menu, self.url)


class Section(models.Model):
    class Meta:
        verbose_name = u"секция"
        verbose_name_plural = u'секции'
        db_table = u'sections'

    name = models.CharField(verbose_name=u'наименование секции', max_length=30, unique=True, db_index=True)
    # section_id = models.CharField(verbose_name=u'id секции', max_length=30, unique=True, db_index=True)
    # section_content = RichTextField(verbose_name=u'HTML контент', max_length=5000)
    enable = models.BooleanField(verbose_name=u'активность секции')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class MailSet(models.Model):
    class Meta:
        verbose_name = u"Шлюз отправки почты"
        verbose_name_plural = u'Шлюзы отправки почты'
        db_table = u'mailsets'

    name = models.CharField(max_length=50, verbose_name=u'название настроек')
    default = models.BooleanField(verbose_name=u'использовать эти настройки для передачи почты', default=False)

    email_host = models.CharField(max_length=50, verbose_name=u'хост', default='smtp.gmail.com')
    email_host_port = models.IntegerField(verbose_name=u'порт', default=587)
    email_use_tls = models.BooleanField(verbose_name=u'использовать защищеное соединение TLS', default=True)
    email_host_user = models.CharField(max_length=50, verbose_name=u'транспортная почта')
    email_host_password = models.CharField(max_length=50, verbose_name=u'транспортный пароль')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def setup(self):
        backend = EmailBackend(host=self.email_host, port=self.email_host_port, username=self.email_host_user,
                               password=self.email_host_password, use_tls=self.email_use_tls)
        return backend

    def save(self, *args, **kwargs):
        MailSet.objects.all().update(default=False)
        super(MailSet, self).save(*args, **kwargs)
