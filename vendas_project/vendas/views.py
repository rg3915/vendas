# -*- coding: utf-8 -*-
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.db.models import F
from .models import Customer, Brand, Product, Sale, SaleDetail


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class CustomerList(ListView):
    template_name = 'customer_list.html'
    model = Customer
    context_object = 'customer_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(CustomerList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class BrandList(ListView):
    template_name = 'brand_list.html'
    model = Brand
    context_object = 'brand_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(BrandList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class ProductList(ListView):
    template_name = 'product_list.html'
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

        if var_get_search is not None:
            cObj = cObj.filter(product__icontains=var_get_search)

        if self.request.GET.get('filter_link', False):
            cObj = cObj.filter(stoq__lt=F('stoq_min'))

        return cObj


class SaleCreate(CreateView):
    template_name = 'sale_form.html'
    model = Sale
    success_url = reverse_lazy('sale_list')


class SaleList(ListView):
    template_name = 'sale_list.html'
    model = Sale
    context_object = 'sale_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(SaleList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class SaleDetailView(TemplateView):
    template_name = 'sale_detail.html'
    model = Sale

    def get_context_data(self, **kwargs):
        Objvenda = Sale.objects.get(pk=self.kwargs['pk'])
        ItensVenda = SaleDetail.objects.all().filter(sale=Objvenda)
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['count'] = ItensVenda.count()
        context['Sale'] = Objvenda
        context['Itens'] = ItensVenda
        return context


class CustomerSearch(ListView):
    template_name = 'search.html'
    model = Customer
    context_object_name = 'lista'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(CustomerSearch, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        cObj = Customer.objects.all()
        var_get_search = self.request.GET.get('search_box')
        var_get_order_by = self.request.GET.get('order')

        if var_get_search is not None:
            cObj = cObj.filter(firstname__icontains=var_get_search)

        if var_get_order_by is not None:
            cObj = cObj.order_by(var_get_order_by)

        return cObj


class CustomerSale(ListView):
    template_name = 'sale_list.html'
    model = Sale
    context_object_name = 'lista'
    paginate_by = 8

    def get_queryset(self):
        cObj = Sale.objects.all()
        var_get_search = self.request.GET.get('customer_sale')

        if var_get_search is not None:
            cObj = cObj.filter(customer__icontains=var_get_search)

        return cObj
