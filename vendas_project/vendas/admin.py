# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from .models import Customer, Seller, Brand, Product, Sale, SaleDetail


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone', 'created')
    date_hierarchy = 'created'
    search_fields = ('firstname', 'lastname')


class SellerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'internal', 'email',
                    'phone', 'created', 'commissioned', 'active')
    date_hierarchy = 'created'
    search_fields = ('firstname', 'lastname')
    list_filter = ('internal', 'commissioned', 'active')


class ProductAdmin(admin.ModelAdmin):
    ordering = ['product']
    list_display = (
        'ncm', 'imported', 'product', 'brand', 'get_price', 'outofline')
    list_filter = ('outofline', 'brand',)
    search_fields = ('product',)


class SaleDetailInline(admin.TabularInline):
    list_display = ['product', 'quantity', 'price_sale']
    # readonly_fields = ['get_subtotal']
    model = SaleDetail
    extra = 0


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'customer', 'created', 'get_itens', 'get_total')
    readonly_fields = ['get_total']
    date_hierarchy = 'created'
    list_filter = ('customer',)
    inlines = [SaleDetailInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
