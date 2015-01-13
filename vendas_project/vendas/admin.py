# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from .models import Customer, Brand, Product, Sale, SaleDetail


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'phone', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('firstname', 'lastname')


class ProductAdmin(admin.ModelAdmin):
    ordering = ['product']
    list_display = ('product', 'brand', 'price')
    list_filter = ('brand',)
    search_fields = ('product',)


class SaleDetailInline(admin.TabularInline):
    list_display = ['product', 'quantity', 'price_sale', 'subtotal']
    model = SaleDetail
    extra = 0


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'customer', 'date_sale', 'get_itens', 'get_total')
    readonly_fields = ['get_total']
    date_hierarchy = 'date_sale'
    list_filter = ('customer',)
    inlines = [SaleDetailInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
