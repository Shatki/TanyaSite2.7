#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

from users.models import User
from .models import Menu
from experience.models import Course
from news.models import Comment, get_news
from gallery.models import Photo
from romanovatatiana.settings import MENU_CHOICES, MENU_DEFAULT, TEMPLATE_PAGE_DEFAULT, TEMPLATE_CONTACTS
from romanovatatiana.settings import NO_PHOTO


def menus():
    menus = Menu.objects.all()
    _menu = []
    for menu in MENU_CHOICES:
        collect = []
        for submenu in menus:
            # print(submenu.menu, menu[0])
            if submenu.menu == menu[0]:
                # print(submenu.name)
                _choice = dict(
                    name=submenu.name,
                    url=submenu.get_url()
                )
                collect.append(_choice)
        elem = dict(
            name=menu[1][0].upper() + menu[1][1:],  # Увеличим первую букву
            menu=menu[0],
            choices=collect
        )
        _menu.append(elem)
    return _menu


# Create your views here.
@csrf_protect
def about(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    args['news_list'] = []

    # Данные по курсам
    args['courses'] = Course.objects.all().order_by('begin_date')

    # Данные по новостям
    for news in get_news()[-3:]:
        try:
            collect = dict(
                id=news.id,
                url=news.absolute_url,
                fix=news.fix,
                title=news.title,
                added=news.added,
                text=news.text,
                photo=news.photo,
                comments=0,
            )
            args['news_list'].append(collect)
        except:
            pass
    comments = Comment.objects.filter(allowed=True)
    for news in args['news_list']:
        for comment in comments:
            if news['id'] == comment.news.id:
                news['comments'] = news['comments'] + 1

    # Данные галлереи
    photos = []
    for _photo in Photo.objects.all().order_by('-added')[:6]:  # Нужно чтоб выдавал последние
        try:
            photo = dict(
                id=_photo.id,
                name=_photo.name,
                url=_photo.url(),
                photo=_photo,
                album=_photo.album.name,
            )
            photos.append(photo)
        except:
            pass
    args['photos'] = photos
    args['NO_PHOTO'] = NO_PHOTO

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response(TEMPLATE_PAGE_DEFAULT, args)


@csrf_protect
def contacts(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    # общее меню
    args['menus'] = menus()

    return render_to_response(TEMPLATE_CONTACTS, args)
