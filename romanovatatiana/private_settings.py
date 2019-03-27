#!/usr/bin/python
# -*- coding: utf-8 -*-
# Email host setup
# Google ограничивает количество исходящих электронных сообщений до 100 штук в день.
URL = 'romanovatatiana.ru'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2i7cv@5e*@((_pi)$c31ix@qb9ivr+ui^hc@4bee(9g6ec_8hs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    u'romanovatatiana.ru',
    u'https://romanovatatiana.ru',
    u'www.romanovatatiana.ru'
    u'9200247477.myjino.ru',
    ]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'crjhgbjy303'
EMAIL_HOST_USER = 'mail.romanovatatiana.ru@gmail.com'
#для Gmail SMTP сервера 465 для SSL и 587 для TSL.
EMAIL_PORT = 587
EMAIL_USE_TLS = True