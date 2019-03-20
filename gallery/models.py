#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from romanovatatiana.settings import GALLERY_PHOTOS_DIR


class Photo(models.Model):
    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
        db_table = u'photos'

    name = models.CharField(max_length=50, verbose_name=u'наименование', null=False)
    description = models.CharField(max_length=50, verbose_name=u'описание', null=True)
    album = models.ForeignKey(u'Album', on_delete=models.CASCADE, null=False,
                              verbose_name=u'принадлежность к альбому')
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    photo = models.ImageField(upload_to=GALLERY_PHOTOS_DIR, verbose_name=u'фотография')

    label = models.BooleanField(u'сделать профильной фотографией альбома', default=False)

    def save(self, *args, **kwargs):
        Photo.objects.filter(album=self.album, label=True).update(label=False)
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def dir(self):
        return self.album

    def get_photo(self):
        return self.photo

    def url(self):
        # return '%s/' % self.directory  # ВРЕМЕННО
        return self.photo.url


class Album(models.Model):
    class Meta:
        verbose_name = u'альбом'
        verbose_name_plural = u'альбомы'
        db_table = u'albums'

    name = models.CharField(max_length=50, verbose_name=u'наименование альбома(рус)', unique=True)
    description = models.CharField(max_length=50, verbose_name=u'описание альбома(не обязательно)', null=True, blank=True)
    directory = models.CharField(max_length=200, verbose_name=u"псевдоним альбома(англ)", unique=True)

    def __str__(self):
        return self.directory

    def __unicode__(self):
        return u'%s' % self.directory

    def url(self):
        # return '%s/' % self.directory  # ВРЕМЕННО
        return u'/%s%s/' % (GALLERY_PHOTOS_DIR, self.directory)  # ВРЕМЕННО
