from django.http import HttpResponse
from .models import Product
import json


def list_products(request):
    allproducts = Product.objects.all()
    allproducts_dics = [p.to_dict_json() for p in allproducts]
    return HttpResponse(json.dumps(allproducts_dics), content_type="application/json")


def cria_pedido(request):
    product_ids = json.loads(request.POST['product_ids'])
    sales_details = _cria_sales_details_a_partir_dos_product_ids(product_ids)
    customer = descobre_o_customer_a_partir_do_usuario_logado(request)
    sale = _cria_sale(customer, sales_details)
    return HttpResponse(json.dumps(sale.to_dict_json()))
