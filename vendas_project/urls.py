# coding: utf-8
from django.conf.urls import patterns, include, url
from vendas.views import *
from vendas.models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'vendas_project.vendas.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='home'),
    url(r'^customer/$', CustomerList.as_view(), name='customer_list'),
    url(r'^category/$', CategoryList.as_view(), name='category_list'),
    url(r'^product/$', ProductList.as_view(), name='product_list'),
    url(r'^sale/$', SaleList.as_view(), name='sale_list'),
    url(r'^sale/(?P<pk>\d+)/$', SaleDetailView.as_view(), name='sale_detail'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^search/$', 'search', name='search'),
    # url(r'^search/$', PessoaList.as_view(), name='search'),
)
