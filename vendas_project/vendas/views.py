# -*- coding: utf-8 -*-
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.db.models import F
from django.db.models import Count
from .models import Customer, Seller, Brand, Product, Sale, SaleDetail


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class FirstnameSearchMixin(object):

    def get_queryset(self):
        queryset = super(FirstnameSearchMixin, self).get_queryset()
        q = self.request.GET.get('search_box')
        if q:
            return queryset.filter(firstname__icontains=q)
        return queryset


class CustomerList(CounterMixin, FirstnameSearchMixin, ListView):
    template_name = 'vendas/person/customer_list.html'
    model = Customer
    paginate_by = 8


class CustomerDetail(DetailView):
    template_name = 'vendas/person/customer_detail.html'
    model = Customer


class SellerList(CounterMixin, FirstnameSearchMixin, ListView):
    template_name = 'vendas/person/seller_list.html'
    model = Seller
    paginate_by = 8


class SellerDetail(DetailView):
    template_name = 'vendas/person/seller_detail.html'
    model = Seller


class BrandList(CounterMixin, ListView):
    template_name = 'vendas/product/brand_list.html'
    model = Brand


class ProductList(CounterMixin, ListView):
    template_name = 'vendas/product/product_list.html'
    model = Product
    paginate_by = 100

    def get_queryset(self):
        p = Product.objects.all()
        q = self.request.GET.get('search_box')
        # buscar por produto
        if q is not None:
            p = p.filter(product__icontains=q)
        # filtra produtos em baixo estoque
        if self.request.GET.get('filter_link', False):
            p = p.filter(stock__lt=F('stock_min'))
        return p


class SaleCreate(CreateView):
    template_name = 'vendas/sale/sale_form.html'
    model = Sale
    success_url = reverse_lazy('sale_list')


class SaleList(CounterMixin, ListView):
    template_name = 'vendas/sale/sale_list.html'
    model = Sale
    paginate_by = 20

    def get_queryset(self):
        # filtra vendas com um item
        if 'filter_sale_one' in self.request.GET:
            return Sale.objects.annotate(
                itens=Count('sales_det')).filter(itens=1)
        # filtra vendas com zero item
        if 'filter_sale_zero' in self.request.GET:
            return Sale.objects.annotate(
                itens=Count('sales_det')).filter(itens=0)
        # filtros no queryset
        qs = super(SaleList, self).get_queryset()
        # clica no cliente e retorna as vendas dele
        if 'customer' in self.request.GET:
            qs = qs.filter(customer=self.request.GET['customer'])
        # clica no vendedor e retorna as vendas dele
        if 'seller' in self.request.GET:
            qs = qs.filter(seller=self.request.GET['seller'])
        return qs


class SaleDetailView(DetailView):
    template_name = 'vendas/sale/sale_detail.html'
    model = Sale
    context_object_name = 'Sale'

    def get_context_data(self, **kwargs):
        sd = SaleDetail.objects.filter(sale=self.object)
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['count'] = sd.count()
        context['Itens'] = sd
        return context
