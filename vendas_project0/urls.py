# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from vendas_project.vendas.views import *
from vendas_project.vendas.models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'vendas_project.vendas.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='home'),
    url(r'^customers/$', CustomerList.as_view(), name='customer_list'),
    url(r'^customers/(?P<pk>\d+)/$',
        CustomerDetail.as_view(), name='customer_detail'),
    url(r'^customers/edit/(?P<pk>\d+)/$',
        CustomerUpdate.as_view(), name='customer_update'),

    url(r'^brand/$', BrandList.as_view(), name='brand_list'),
    url(r'^product/$', ProductList.as_view(), name='product_list'),

    url(r'^sale/add/$', SaleCreate.as_view(), name='sale_add'),
    url(r'^sale/$', SaleList.as_view(), name='sale_list'),
    url(r'^sale/(?P<pk>\d+)/$', SaleDetailView.as_view(), name='sale_detail'),
    url(r'^sellers/$', SellerList.as_view(), name='seller_list'),
    url(r'^sellers/(?P<pk>\d+)/$',
        SellerDetail.as_view(), name='seller_detail'),

    url(r'^about/$', About.as_view(), name='about'),
)
urlpatterns += patterns(
    'vendas_project.vendas.json_views',
    url(r'^api/list_products$', 'list_products', name='api_list_products'),
    url(r'^api/cria_pedido$', 'cria_pedido', name='api_cria_pedido'),

)
