from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'core.views',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^customers/$', CustomerList.as_view(), name='customer_list'),
    url(r'^customers/(?P<pk>\d+)/$',
        CustomerDetail.as_view(), name='customer_detail'),
    url(r'^customers/edit/(?P<pk>\d+)/$',
        CustomerUpdate.as_view(), name='customer_update'),

    url(r'^brand/$', BrandList.as_view(), name='brand_list'),
    url(r'^product/$', ProductList.as_view(), name='product_list'),

    url(r'^sale/add/$', sale_create, name='sale_add'),
    url(r'^sale/$', SaleList.as_view(), name='sale_list'),
    url(r'^sale/(?P<pk>\d+)/$', SaleDetailView.as_view(), name='sale_detail'),
    url(r'^sellers/$', SellerList.as_view(), name='seller_list'),
    url(r'^sellers/(?P<pk>\d+)/$',
        SellerDetail.as_view(), name='seller_detail'),

    url(r'^about/$', About.as_view(), name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
