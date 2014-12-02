# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .models import Customer, Category, Product, Sale, SaleDetail
from .forms import ProductFilter


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


class CategoryList(ListView):
    template_name = 'category_list.html'
    model = Category
    context_object = 'category_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object = 'product_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):

        context = super(ProductList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class SaleList(ListView):
    template_name = 'sale_list.html'
    model = Sale
    context_object = 'sale_list'
    paginate_by = 8

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


class ProductSearch(ListView):
    template_name = 'search.html'
    model = Product
    context_object_name = 'lista'
    paginate_by = 8

    def get_queryset(self):
        pObj = Product.objects.all()
        var_get_search = self.request.GET.get('search_box')
        var_get_order_by = self.request.GET.get('order')

        if var_get_search is not None:
            pObj = pObj.filter(product__icontains=var_get_search)

        if var_get_order_by is not None:
            pObj = pObj.order_by(var_get_order_by)

        return pObj
