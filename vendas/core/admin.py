from django.contrib import admin
from .models import Customer, Seller, Brand, Product, Sale, SaleDetail


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpf', 'email', 'phone', 'birthday', 'created')
    date_hierarchy = 'created'
    search_fields = ('firstname', 'lastname')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'internal', 'email',
                    'phone', 'created', 'commissioned', 'active')
    date_hierarchy = 'created'
    search_fields = ('firstname', 'lastname')
    list_filter = ('internal', 'commissioned', 'active')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['product']
    list_display = (
        'ncm', 'imported', 'product', 'brand', 'get_price', 'outofline')
    list_filter = ('outofline', 'brand',)
    search_fields = ('product',)


class SaleDetailInline(admin.TabularInline):
    list_display = ['product', 'quantity', 'price_sale']
    readonly_fields = ['get_subtotal']
    model = SaleDetail
    extra = 0


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'customer', 'created', 'get_itens', 'get_total')
    readonly_fields = ['get_total']
    date_hierarchy = 'created'
    list_filter = ('customer',)
    inlines = [SaleDetailInline]


admin.site.register(Brand)
