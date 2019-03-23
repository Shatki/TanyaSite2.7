#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Django settings for romanovatatiana project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2i7cv@5e*@((_pi)$c31ix@qb9ivr+ui^hc@4bee(9g6ec_8hs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'website',
    'gallery',
    'users',
    'pages',
    'news',
    'experience',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'romanovatatiana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'romanovatatiana.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

URL = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
MEDIA_URL = '/media/'

STATIC_IMAGE_DIR = 'img/'
CONTENT_PICS_DIR = 'content/'
PROFILE_PHOTOS_DIR = 'photos/'
HEADER_PHOTOS_DIR = 'headers/'
GALLERY_PHOTOS_DIR = 'gallery/'
AWARDS_PHOTOS_DIR = 'awards/'
NEWS_PHOTOS_DIR = 'news/'
DOCUMENTS_DIR = 'documents/'
DOCUMENTS_MINIATURES_DIR = 'miniatures/'

CONTENT_PIC_DEFAULT_NAME = CONTENT_PICS_DIR + 'image.jpg'
PROFILE_PHOTO_DEFAULT_NAME = PROFILE_PHOTOS_DIR + 'profileimage.jpg'
HEADER_PHOTO_DEFAULT_NAME = HEADER_PHOTOS_DIR + 'header.jpg'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  'files', 'static'),
)

# Application definition
AUTH_USER_MODEL = 'users.User'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# CKEDITOR_CONFIGS по сути необязательны. Они влияют на тулбар редактора. Если выключите - будет очень мало
# инструментов для работы с текстом. После полной настройки - попробуйте с ними поиграться. Возможно найдете для себя
# какой-то более оптимальный вариант настроек!
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
             'RemoveFormat'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'sourcearea', 'SpecialChar'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Maximize', 'ShowBlocks']
        ],
    }
}

PAGINATION_NEWS_ON_PAGE = 3  # Количество новостей на странице
PAGINATION_LIST_RANGE = 3  # Число страниц отопбажаемых в строке пагинация между u"Назад" и u"Вперед"

# Корневое меню
ABOUT = u'about'
GROUP = u'group'
DOCS = u'documents'
NEWS = u'news'
CONTACTS = u'contacts'
GALLERY = u'gallery'
PARENTS = u'parents'
METHODIC = u'methodic'

MENU_DEFAULT = ABOUT

MENU_CHOICES = (
    (ABOUT, u'обо мне'),
    (DOCS, u'документы'),
    (GROUP, u'группа'),
    (PARENTS, u'для родителей'),
    (METHODIC, u'мои разработки'),
    (NEWS, u'новости'),
    (GALLERY, u'фотогалерея'),
    (CONTACTS, u'контакты'),
)

# Награды
GRATEFUL = u'grateful'
LETTER = u'letter'
DIPLOM = u'diplom'
QUALIFICATION = u'qualification'
CERTIFICATE = u'certificate'

AWARDS_CHOICES = (
    (GRATEFUL, u'благодарность'),
    (LETTER, u'грамота'),
    (DIPLOM, u'диплом'),
    (QUALIFICATION, u'удостоверение'),
    (CERTIFICATE, u'сертификат'),
)

PDF = u'pdf'
PPT = u'ppt'
PPTX = u'pptx'
XLS = u'xls'
XLSX = u'xlsx'
DOC = u'doc'
DOCX = u'docx'
UNKNOWN = u'unknown'

DOCUMENT_TYPES = (
    (PDF, u'*.pdf файл Adobe Reader'),
    (PPT, u'*.ppt файл презентации MS PowerPoint 97/2003'),
    (PPTX, u'*.pptx файл презентации MS PowerPoint'),
    (DOC, u'*.doc текстовый файл MS Word 97/2003'),
    (DOCX, u'*.docx текстовый файл MS Word'),
    (XLS, u'*.xls файл электронных таблиц MS Excel 97/2003'),
    (XLSX, u'*.xlsx файл электронных таблиц MS Excel'),
    (UNKNOWN, u'неизвестный тип файла'),
)

EDITOR = u'editor'
SPECIAL = u'special'
NULL_PAGE = u'null_page'

PAGE_TYPES = (
    (NULL_PAGE, u'Страница еще не создана'),
    (SPECIAL, u'Специализированная страница без выбора типа контента'),
    (DOCS, u'Страница с документами'),
    (EDITOR, u'Страница с редактированием текста'),
)


# statics
NO_PHOTO = STATIC_IMAGE_DIR + 'nophoto.png'
DOCUMENT_PDF_MINIATURE = STATIC_IMAGE_DIR + 'pdf.png'
DOCUMENT_EXCEL_MINIATURE = STATIC_IMAGE_DIR + 'excel.png'
DOCUMENT_POWERPOINT_MINIATURE = STATIC_IMAGE_DIR + 'powerpoint.png'
DOCUMENT_WORD_MINIATURE = STATIC_IMAGE_DIR + 'word.png'
DOCUMENT_UNKNOWN_MINIATURE = STATIC_IMAGE_DIR + 'unknown.png'


# Виды шаблонов страниц
TEMPLATE_PAGE_DEFAULT = u'about.html'
TEMPLATE_DOCUMENTS = u'documents.html'
TEMPLATE_AWARDS = u'awards.html'
TEMPLATE_EDITOR = u'editor.html'
TEMPLATE_CONTACTS = u'contacts.html'
TEMPLATE_NEWS_LIST = u'news__list.html'
TEMPLATE_NEWS_DETAIL = u'news__detail.html'
TEMPLATE_NO_PAGE = u'404.html'


