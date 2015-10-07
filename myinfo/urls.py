# -*- coding: utf-8 -*-
__author__ = 'Юля'

from django.conf.urls import patterns, url
from myinfo.views import index

urlpatterns = patterns('',
                       url(r'^$', index),
                       )
