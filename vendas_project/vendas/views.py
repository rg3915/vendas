from django.views.generic import TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Customer, Category, Product, Sale, SaleDetail


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class CustomerList(ListView):
    template_name = 'customer_list.html'
    model = Customer
    context_object = 'customer_list'
    paginate_by = 10


class CategoryList(ListView):
    template_name = 'category_list.html'
    model = Category
    context_object = 'category_list'
    paginate_by = 10


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object = 'product_list'
    paginate_by = 10


class SaleList(ListView):
    template_name = 'sale_list.html'
    model = Sale
    context_object = 'sale_list'
    paginate_by = 10


class SaleDetailView(DetailView):
    template_name = 'sale_detail.html'
    # model = Venda
