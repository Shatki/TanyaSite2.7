#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tatyana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sys import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from experience.views import awards
from users.views import feedback
from pages.views import page_dispatcher
from website.views import about, contacts
from gallery.views import gallery_list, gallery_detail
from news.views import news_list, news_detail, comment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/awards/', awards),
    url(r'^about/', about),
    url(r'^contacts/feedback/', feedback),
    url(r'^contacts/', contacts),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^gallery/(?P<directory>\w+)/$', gallery_detail),
    url(r'^gallery/', gallery_list),
    url(r'^news/(?P<news_id>\d+)/comment/', comment),
    url(r'^news/(?P<news_id>\d+)/', news_detail),
    url(r'^news/', news_list),

    url('^(?P<menu>\w+)/(?P<url>\w+)/', page_dispatcher),
    url(r'^$', about),
    # path('users/<username>/photo/', users.get_photo),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
