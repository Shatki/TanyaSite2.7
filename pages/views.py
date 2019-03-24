#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from website.views import menus
from users.models import User
from .models import Menu
from pages.models import Document, Editor
from romanovatatiana.settings import MENU_DEFAULT, TEMPLATE_DOCUMENTS, TEMPLATE_NO_PAGE, TEMPLATE_EDITOR
from romanovatatiana.settings import DOCUMENT_PDF_MINIATURE, DOCUMENT_EXCEL_MINIATURE, DOCUMENT_POWERPOINT_MINIATURE, \
    DOCUMENT_WORD_MINIATURE, DOCUMENT_UNKNOWN_MINIATURE, NO_PHOTO, URL
from romanovatatiana.settings import PPTX, PDF, PPT, XLS, XLSX, DOC, DOCX, UNKNOWN

from romanovatatiana.settings import DOCS, EDITOR


# Create your views here.
def documents(args, url):
    args['documents'] = ""
    args['DOCUMENT_PDF_MINIATURE'] = DOCUMENT_PDF_MINIATURE
    args['DOCUMENT_EXCEL_MINIATURE'] = DOCUMENT_EXCEL_MINIATURE
    args['DOCUMENT_WORD_MINIATURE'] = DOCUMENT_WORD_MINIATURE
    args['DOCUMENT_POWERPOINT_MINIATURE'] = DOCUMENT_POWERPOINT_MINIATURE
    args['DOCUMENT_UNKNOWN_MINIATURE'] = DOCUMENT_UNKNOWN_MINIATURE
    args['PDF'] = PDF
    args['UNKNOWN'] = UNKNOWN
    args['PPT'] = PPT
    args['PPTX'] = PPTX
    args['XLS'] = XLS
    args['XLSX'] = XLSX
    args['DOC'] = DOC
    args['DOCX'] = DOCX
    args['URL'] = URL
    args['page'].header = '/static/img/cell-phone-close.jpg'  # editor.header.url
    template = TEMPLATE_DOCUMENTS
    try:
        docs = Document.objects.filter(page__url=url, allowed=True).order_by('-added')
        args['documents'] = docs
    except:
        return args, TEMPLATE_NO_PAGE
    # Вызов конструктор страниц
    return args, template


def editors(args, url):
    try:
        editor = Editor.objects.get(page__url=url, allowed=True)
        args['page'].text = editor.text
        args['page'].title = editor.title
        args['page'].header = editor.header.url
    except Editor.DoesNotExist:
        return args, TEMPLATE_NO_PAGE
    return args, TEMPLATE_EDITOR


@csrf_protect
def page_dispatcher(request, menu, url):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    # общее меню
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    # переход с меню
    args['menu'] = menu
    args['page'] = ""
    template = TEMPLATE_NO_PAGE

    try:
        page = Menu.objects.get(url=url)
        args['page'] = page
    except Menu.DoesNotExist:
        return render_to_response(template, args)

    if args['page'].page == DOCS:
        args, template = documents(args, url)

    if args['page'].page == EDITOR:
        args, template = editors(args, url)

    return render_to_response(template, args)
