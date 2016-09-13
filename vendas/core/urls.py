from django.conf.urls import include, url
from vendas.core import views as c

customer_patterns = [
    url(r'^$', c.CustomerList.as_view(), name='customer_list'),
    url(r'^(?P<pk>\d+)/$', c.CustomerDetail.as_view(), name='customer_detail'),
    url(r'^edit/(?P<pk>\d+)/$', c.CustomerUpdate.as_view(), name='customer_update'),
]
brand_patterns = [
    url(r'^$', c.BrandList.as_view(), name='brand_list'),
]

product_patterns = [
    url(r'^$', c.ProductList.as_view(), name='product_list'),
]

sale_patterns = [
    url(r'^add/$', c.sale_create, name='sale_add'),
    url(r'^$', c.SaleList.as_view(), name='sale_list'),
    url(r'^(?P<pk>\d+)/$', c.SaleDetailView.as_view(), name='sale_detail'),
]

seller_patterns = [
    url(r'^$', c.SellerList.as_view(), name='seller_list'),
    url(r'^(?P<pk>\d+)/$', c.SellerDetail.as_view(), name='seller_detail'),
]

urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^about/$', c.about, name='about'),
    url(r'^customer/', include(customer_patterns)),
    url(r'^brand/', include(brand_patterns)),
    url(r'^product/', include(product_patterns)),
    url(r'^sale/', include(sale_patterns)),
    url(r'^seller/', include(seller_patterns)),
]
