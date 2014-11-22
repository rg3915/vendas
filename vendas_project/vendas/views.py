#from simple_search import generic_search, perform_search
from django.views.generic import TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect, get_object_or_404
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


class SaleDetailView(DetailView):
    template_name = 'sale_detail.html'
    model = Sale

# QUERY = "search-query"

# MODEL_MAP = {
#     Product: ["product"],
#     Customer: ["firstname", "lastname"],
# }


# def search(request):
#     objects = []
#     for model, fields in MODEL_MAP.iteritems():
#         objects += generic_search(request, model, fields, QUERY)

#     return render_to_response("search_results.html",
#                               {
#                                   "objects": objects, "search_string": request.GET.get(QUERY, ""),
#                               })


# def list_products(request, category_pk):
#     query_string = request.GET.get(QUERY, "").strip()
#     category = get_object_or_404(Category, pk=category_pk)
#     products = Product.objects.filter(category=category)
#     products = perform_search(query_string, products, MODEL_MAP['Product'])

#     return render_to_response("product_list.html",
#                               {
#                                   "products": products,
#                                   "search_string": query_string,
#                               })

# def search(request):

#     if request.GET:
#         form = ProductSearchForm(request.GET)
#         if form.is_valid():
#             results = form.get_result_queryset()
#         else:
#             results = []
#     else:
#         form = ProductSearchForm()
#         results = []

#     return render_to_response(
#         'search.html',
#         RequestContext(request, {
#             'form': form,
#             'results': results,
#         })
#     )

def product_list(request):
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render_to_response('search.html', {'filter': filter})
    # return render_to_response('product_list.html', {'filter': filter})
