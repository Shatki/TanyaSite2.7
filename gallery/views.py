#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from .models import Album, Photo
from romanovatatiana.settings import NO_PHOTO, MENU_DEFAULT
from website.views import menus
from users.models import User
from django.template.context_processors import csrf


# Create your views here.
@csrf_protect
def gallery_list(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args[u'username'] = auth.get_user(request).username
        args[u'profile'] = auth.get_user(request).photo

    args[u'photo'] = User.objects.get(is_superuser=True).photo
    args[u'menus'] = menus()
    args[u'menu_default'] = MENU_DEFAULT
    args[u'result'] = True
    albums = []
    for _object in Album.objects.all():
        try:
            _photo = Photo.objects.get(album_id=_object.id, label=True)
        except Photo.DoesNotExist:
            _photo = None
        else:
            _photo = _photo.photo.url
        album = dict(
            id=_object.id,
            name=_object.name,
            url=_object.url(),
            photo=_photo
        )
        albums.append(album)
    args[u'albums'] = albums
    args[u'NO_PHOTO'] = NO_PHOTO
    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response(u'gallery_list.html', args)


@csrf_protect
def gallery_detail(request, directory):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args[u'username'] = auth.get_user(request).username
        args[u'profile'] = auth.get_user(request).photo

    args[u'photo'] = User.objects.get(is_superuser=True).photo
    args[u'menus'] = menus()
    args[u'menu_default'] = MENU_DEFAULT
    args[u'result'] = True
    try:
        album = Album.objects.get(directory=directory)
        photos = Photo.objects.filter(album=album)
        # print(photos)
        args[u'album'] = album
        args[u'photos'] = photos
    except Album.DoesNotExist:
        args[u'result'] = u'DB Query error: gallery album does not exist'
    except Photo.DoesNotExist:
        args[u'result'] = u'DB Query error: gallery photos does not exist'

    return render_to_response(u'gallery_detail.html', args)
