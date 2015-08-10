# -*- coding: utf-8 -*-
from model_mommy import mommy
from vendas_project.vendas.models import Customer, Product, Sale, SaleDetail
import names

customers = mommy.make(
    Customer, firstname=names.get_first_name, lastname=names.get_last_name, _quantity=10)
products = mommy.make(Product, _quantity=20)
sales = mommy.make(Sale, _quantity=10)
saledetails = mommy.make(SaleDetail, _quantity=100)
