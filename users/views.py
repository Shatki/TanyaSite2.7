#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

from .models import User
from romanovatatiana.settings import STATIC_URL, PROFILE_PHOTO_DEFAULT_NAME, PROFILE_PHOTOS_DIR


# Create your views here.
@csrf_protect
def get_photo(request, username):
    # Тут код отдачи фотографии
    try:
        user = User.objects.get(username=username)
        photo = user.get_photo().path
    except:
        return redirect(os.path.join(PROFILE_PHOTOS_DIR, PROFILE_PHOTO_DEFAULT_NAME))

    # print(os.path.join(PROFILE_PHOTOS_DIR, photo))
    return redirect(os.path.join(STATIC_URL, PROFILE_PHOTOS_DIR + photo))
