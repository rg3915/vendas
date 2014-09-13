# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Cliente, Categoria, Produto, Venda, DetVenda


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class ClientList(ListView):
    template_name = 'client_list.html'
    model = Cliente
    context_object = 'client_list'
    paginate_by = 10


class CategoryList(ListView):
    template_name = 'category_list.html'
    model = Categoria
    context_object = 'category_list'
    paginate_by = 10


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Produto
    context_object = 'product_list'
    paginate_by = 10


class SaleList(ListView):
    template_name = 'sale_list.html'
    model = Venda
    context_object = 'sale_list'
    paginate_by = 10


class SaleDetailView(DetailView):
    template_name = u'sale_detail.html'
    model = Venda
    context_object_name = 'sale'
