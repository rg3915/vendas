from django.urls import include, path
from vendas.core import views as c


app_name = 'core'


customer_patterns = [
    path('', view=c.CustomerList.as_view(), name='customer_list'),
    path('<int:pk>/', view=c.CustomerDetail.as_view(), name='customer_detail'),
    path('edit/<int:pk>/', view=c.CustomerUpdate.as_view(), name='customer_update'),
]

brand_patterns = [
    path('', view=c.BrandList.as_view(), name='brand_list'),
]

product_patterns = [
    path('', view=c.ProductList.as_view(), name='product_list'),
]

sale_patterns = [
    path('', view=c.SaleList.as_view(), name='sale_list'),
    path('add/', view=c.sale_create, name='sale_add'),
    path('<int:pk>/', view=c.SaleDetailView.as_view(), name='sale_detail'),
]

seller_patterns = [
    path('', view=c.SellerList.as_view(), name='seller_list'),
    path('<int:pk>/', view=c.SellerDetail.as_view(), name='seller_detail'),
]

urlpatterns = [
    path('', c.home, name='home'),
    path('about/', c.about, name='about'),
    path('customer/', include(customer_patterns)),
    path('brand/', include(brand_patterns)),
    path('product/', include(product_patterns)),
    path('sale/', include(sale_patterns)),
    path('seller/', include(seller_patterns)),
]
