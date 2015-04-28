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


class CustomerList(ListView):
    template_name = 'vendas/person/customer_list.html'
    model = Customer
    context_object = 'customer_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(CustomerList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        cObj = Customer.objects.all()
        var_get_search = self.request.GET.get('search_box')
        # buscar por nome
        if var_get_search is not None:
            cObj = cObj.filter(firstname__icontains=var_get_search)
        return cObj


class CustomerDetail(DetailView):
    template_name = 'vendas/person/customer_detail.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        customer = Customer.objects.get(pk=self.kwargs['pk'])
        return context


class SellerList(ListView):
    template_name = 'vendas/person/seller_list.html'
    model = Seller
    context_object = 'seller_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(SellerList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        s = Seller.objects.all()
        var_get_search = self.request.GET.get('search_box')
        # buscar por nome
        if var_get_search is not None:
            s = s.filter(firstname__icontains=var_get_search)
        return s


class SellerDetail(DetailView):
    template_name = 'vendas/person/seller_detail.html'
    model = Seller

    def get_context_data(self, **kwargs):
        context = super(SellerDetail, self).get_context_data(**kwargs)
        seller = Seller.objects.get(pk=self.kwargs['pk'])
        return context


class BrandList(ListView):
    template_name = 'vendas/product/brand_list.html'
    model = Brand
    context_object = 'brand_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BrandList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class ProductList(ListView):
    template_name = 'vendas/product/product_list.html'
    model = Product
    context_object = 'product_list'
    paginate_by = 100

    def get_context_data(self, **kwargs):

        context = super(ProductList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        cObj = Product.objects.all()
        var_get_search = self.request.GET.get('search_box')
        # buscar por produto
        if var_get_search is not None:
            cObj = cObj.filter(product__icontains=var_get_search)
        # filtra produtos em baixo estoque
        if self.request.GET.get('filter_link', False):
            cObj = cObj.filter(stock__lt=F('stock_min'))

        return cObj


class SaleCreate(CreateView):
    template_name = 'vendas/sale/sale_form.html'
    model = Sale
    success_url = reverse_lazy('sale_list')


class SaleList(ListView):
    template_name = 'vendas/sale/sale_list.html'
    model = Sale
    context_object = 'sale_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(SaleList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        qs = super(SaleList, self).get_queryset()
        # clica no cliente e retorna as vendas dele
        if 'customer' in self.request.GET:
            qs = qs.filter(customer=self.request.GET['customer'])
        # clica no vendedor e retorna as vendas dele
        if 'seller' in self.request.GET:
            qs = qs.filter(seller=self.request.GET['seller'])
        # filtra vendas com zero item
        if 'filter_sale_zero' in self.request.GET:
            qs = Sale.objects.annotate(
                itens=Count('sales_det')).filter(itens=0)
        # filtra vendas com um item
        if 'filter_sale_one' in self.request.GET:
            qs = Sale.objects.annotate(
                itens=Count('sales_det')).filter(itens=1)
        return qs


class SaleDetailView(TemplateView):
    template_name = 'vendas/sale/sale_detail.html'
    model = Sale

    def get_context_data(self, **kwargs):
        Objvenda = Sale.objects.get(pk=self.kwargs['pk'])
        ItensVenda = SaleDetail.objects.all().filter(sale=Objvenda)
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['count'] = ItensVenda.count()
        context['Sale'] = Objvenda
        context['Itens'] = ItensVenda
        return context
