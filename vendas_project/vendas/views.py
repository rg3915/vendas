# coding: utf-8
from django.views.generic import TemplateView, ListView
from .models import Cliente, Categoria, Produto


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
