#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from .models import News, Comment, get_news
from romanovatatiana.settings import PAGINATION_NEWS_ON_PAGE, PAGINATION_LIST_RANGE, MENU_DEFAULT, TEMPLATE_NEWS_LIST, TEMPLATE_NEWS_DETAIL

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.views import menus
from users.models import User

# Create your views here.
from django.template.context_processors import csrf


@csrf_protect
def comment(request, news_id):
    response = True
    try:
        news = Comment.objects.create(
            author=request.POST[u'form-news-reply-name'],
            email=request.POST[u'form-news-reply-email'],
            news_id=news_id,
            message=u'<p>%s</p>' % request.POST[u'form-news-reply-message'],
        )
        try:
            news.reply_id = request.POST[u'form-news-reply-comment']
        except:
            news.reply_id = None
        news.save()
    except:
        response = False

    return JsonResponse(response, safe=False)


@csrf_protect
def news_detail(request, news_id):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args[u'username'] = auth.get_user(request).username
        args[u'profile'] = auth.get_user(request).photo

    args[u'photo'] = User.objects.get(is_superuser=True).photo
    args[u'menus'] = menus()
    args[u'menu_default'] = MENU_DEFAULT
    args[u'result'] = True
    news = []
    try:
        news = News.objects.get(id=news_id)
    except:
        args[u'result'] = False
    args[u'news'] = news
    _comments = Comment.objects.filter(news_id=news_id, allowed=True)
    # добавка чтобы реплика была адресно
    for _comment in _comments:
        if _comment.reply:
            _comment.message = u"%s<a href='#%s'>%s</a>, %s" \
                               % (_comment.message[:3], _comment.reply.id, _comment.reply.author, _comment.message[3:])

    args[u'comments'] = _comments
    return render_to_response(TEMPLATE_NEWS_DETAIL, args)



@csrf_protect
def news_list(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args[u'username'] = auth.get_user(request).username
        args[u'profile'] = auth.get_user(request).photo

    args[u'photo'] = User.objects.get(is_superuser=True).photo
    args[u'menus'] = menus()
    args[u'menu_default'] = MENU_DEFAULT
    args[u'result'] = True

    paginator = Paginator(get_news(), PAGINATION_NEWS_ON_PAGE)

    page = request.GET.get(u'page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_list = paginator.page(paginator.num_pages)

    if paginator.num_pages > PAGINATION_LIST_RANGE * 2 + 1:
        list_start = news_list.number - PAGINATION_LIST_RANGE
        list_end = news_list.number + PAGINATION_LIST_RANGE

        if list_start < 1:
            list_start = 1
            list_end = PAGINATION_LIST_RANGE * 2 + 1

        if list_end > paginator.num_pages:
            list_start = paginator.num_pages - PAGINATION_LIST_RANGE * 2
            list_end = paginator.num_pages

        news_list.list_range = range(list_start, list_end + 1)
    else:
        news_list.list_range = range(1, paginator.num_pages + 1)

    args[u'news_list'] = news_list
    return render_to_response(TEMPLATE_NEWS_LIST, args)
