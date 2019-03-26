#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from romanovatatiana.settings import NEWS_PHOTOS_DIR, PROFILE_PHOTOS_DIR, NEWS, NO_PHOTO
from users.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class News(models.Model):
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        db_table = u'news'

    title = models.CharField(max_length=50, verbose_name=u'заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    photo = models.ImageField(upload_to=NEWS_PHOTOS_DIR, verbose_name=u'фотография', name='photo', blank=False)
    # пока не будем делать
    # tags = models.ManyToManyField(Tags,verbose_name=u'теги')

    fix = models.BooleanField(u'закрепить новость как основную', default=False, blank=True)
    text = RichTextField(verbose_name=u'текст новости')

    def save(self, *args, **kwargs):
        News.objects.all().update(fix=False)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    def url(self):
        return u'%s/%s/' % (NEWS, self.id)

    def absolute_url(self):
        return u'/%s/%s/' % (NEWS, self.id)

    def date(self):
        return u'{:0>2}/{:0>2}/{:0>2}'.format(str(self.added.day), str(self.added.month), str(self.added.year))


class Comment(models.Model):
    class Meta:
        verbose_name = u'комментарий'
        verbose_name_plural = u'комментарии'
        db_table = u'comments'

    # комментатор
    author = models.CharField(max_length=50, verbose_name=u'имя комментатора')
    email = models.EmailField(verbose_name=u'электронная почта')
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)
    news = models.ForeignKey(News, verbose_name=u'комментируемая новость', on_delete=models.CASCADE,
                             blank=False, null=False)
    reply = models.ForeignKey('self', verbose_name=u'ответ на комментарий', on_delete=models.CASCADE,
                              blank=True, null=True)
    message = RichTextField(verbose_name=u'текст комментария', blank=False, null=False)
    photo = models.ImageField(upload_to=PROFILE_PHOTOS_DIR, verbose_name=u'фотография профиля', blank=True)

    def __str__(self):
        return u'%s %s' % (self.added, self.author)

    def __unicode__(self):
        return u'%s %s' % (self.added, self.author)

    def save(self, *args, **kwargs):
        try:
            self.photo = User.objects.get(email=self.email).photo
        except User.DoesNotExist:
            self.photo = None
        super(Comment, self).save(*args, **kwargs)


def get_news():
    news = News.objects.all().order_by('added')
    # Сортировка новостей
    news_sort = []
    fix = None
    for _news in news:
        if _news.fix:
            fix = _news
        else:
            news_sort.append(_news)

    if fix is not None:
        news_sort.append(fix)

    news_sort.reverse()
    return news_sort
