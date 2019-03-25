#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from users.models import User
from romanovatatiana.settings import DOCUMENTS_DIR, DOCUMENTS_MINIATURES_DIR, DOCUMENT_TYPES
from romanovatatiana.settings import HEADER_PHOTOS_DIR
from romanovatatiana.settings import PPTX, PDF, PPT, XLS, XLSX, DOC, DOCX, UNKNOWN
from website.models import Menu
from ckeditor.fields import RichTextField


# Create your models here.
class Document(models.Model):
    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы'
        db_table = u'documents'

    # комментатор
    title = models.CharField(max_length=100, verbose_name=u'Наименование документа',
                             unique=True, blank=False, null=False)
    description = models.CharField(max_length=200, verbose_name=u'Наименование отражаемое на сайте',
                                   unique=True, blank=True, null=True)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=u'Кто добавил/автор документа', on_delete=models.CASCADE)

    doc = models.FileField(upload_to=DOCUMENTS_DIR, verbose_name=u'документ')

    preview = models.ImageField(upload_to=DOCUMENTS_MINIATURES_DIR, verbose_name=u'миниатюра документа',
                                blank=True, default=None)
    page = models.ForeignKey(Menu, verbose_name=u'размещение документа',
                             on_delete=models.CASCADE, blank=False, null=False)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)
    type = models.CharField(max_length=7, verbose_name=u'тип документа', choices=DOCUMENT_TYPES, default=PDF)

    def __str__(self):
        return u'%s %s' % (self.added, self.author)

    def __unicode__(self):
        return u'%s %s' % (self.added, self.author)

    def save(self, *args, **kwargs):
        # print(self.doc.url[-4:])
        if self.doc.url[-3:].lower() == PDF:
            self.type = PDF
        elif self.doc.url[-3:].lower() == PPT:
            self.type = PPT
        elif self.doc.url[-3:].lower() == DOC:
            self.type = DOC
        elif self.doc.url[-3:].lower() == XLS:
            self.type = XLS
        elif self.doc.url[-4:].lower() == PPTX:
            self.type = PPTX
        elif self.doc.url[-4:].lower() == DOCX:
            self.type = DOCX
        elif self.doc.url[-4:].lower() == XLSX:
            self.type = XLSX
        else:
            self.type = UNKNOWN
        # Photo.objects.filter(album=self.album, label=True).update(label=False)
        # print('type:' + self.doc.url[-3:])
        super(Document, self).save(*args, **kwargs)


class Editor(models.Model):
    class Meta:
        verbose_name = u'текстовая страница'
        verbose_name_plural = u'текстовые страницы'
        db_table = u'editors'

    title = models.CharField(max_length=100, verbose_name=u'Основное наименование редактируемой страницы',
                             unique=True, blank=False, null=False)
    description = models.CharField(max_length=200, verbose_name=u'Дополнение к названию страницы',
                                   blank=False, null=False)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=u'Кто добавил/автор текста', on_delete=models.CASCADE, null=False)

    text = RichTextField(verbose_name=u'редактированный текст')

    page = models.ForeignKey(Menu, verbose_name=u'размещение документа',
                             on_delete=models.CASCADE, blank=False, null=False)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)

    header = models.FileField(upload_to=HEADER_PHOTOS_DIR, verbose_name=u'фотография в шапке страницы', null=True)

    def __str__(self):
        return u'%s %s' % (self.title, self.description)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.description)
