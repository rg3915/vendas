# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from .models import Customer, Category, Product, Sale, SaleDetail


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'phone', 'created_at')
    date_hierarchy = 'created_at'


class ProductAdmin(admin.ModelAdmin):
    ordering = ['product']
    list_display = ('product', 'category', 'price')


class SaleDetailInline(admin.TabularInline):
    list_display = ['product', 'quantity', 'price_sale', 'subtotal']
    readonly_fields = ['subtotal']
    model = SaleDetail
    extra = 0


# teste
# class TotalChangeList(ChangeList):
# fields_to_total = ['preco']  # deveria ser 'total' mas está dando erro

#     def get_total_values(self, queryset):
#         total = Venda()
#         total.custom_alias_name = "Totals"
#         for field in self.fields_to_total:
#             setattr(
#                 total, field, queryset.aggregate(Sum(field)).items()[0][1])
#         return total

#     def get_results(self, request):
#         super(TotalChangeList, self).get_results(request)
#         total = self.get_total_values(self.query_set)
#         len(self.result_list)
#         self.result_list._result_cache.append(total)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer', '__unicode__', 'total')
    readonly_fields = ['total']
    inlines = [SaleDetailInline]

    # def get_changelist(self, request, **kwargs):
    #     return TotalChangeList


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
