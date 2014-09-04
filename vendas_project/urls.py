# coding: utf-8
from django.conf.urls import patterns, include, url
from vendas.views import *
from vendas.models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index.as_view(), name='home'),
    url(r'^sobre/$', sobre.as_view(), name='sobre'),
)
