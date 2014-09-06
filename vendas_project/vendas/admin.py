# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from .models import Cliente, Categoria, Produto, Venda, DetVenda


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'fone', 'criado_em')
    date_hierarchy = 'criado_em'


class ProdutoAdmin(admin.ModelAdmin):
    ordering = ['produto']
    list_display = ('produto', 'categoria', 'preco')


class DetVendaInline(admin.TabularInline):
    list_display = ['produto', 'quantidade', 'precovenda', 'subtotal']
    readonly_fields = ['subtotal']
    model = DetVenda
    extra = 0


class TotalChangeList(ChangeList):
    fields_to_total = ['preco']  # deveria ser 'total' mas está dando erro

    def get_total_values(self, queryset):
        total = Venda()
        total.custom_alias_name = "Totals"
        for field in self.fields_to_total:
            setattr(
                total, field, queryset.aggregate(Sum(field)).items()[0][1])
        return total

    def get_results(self, request):
        super(TotalChangeList, self).get_results(request)
        total = self.get_total_values(self.query_set)
        len(self.result_list)
        self.result_list._result_cache.append(total)


class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', '__unicode__', 'total', 'preco')
    readonly_fields = ['total']
    inlines = [DetVendaInline]

    def get_changelist(self, request, **kwargs):
        return TotalChangeList


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
