'''
Calculando total
'''

from vendas_project.vendas.models import SaleDetail
from django.db.models import Sum, F, FloatField
''' ------------ '''
q = SaleDetail.objects.filter(sale=1).values('price_sale', 'quantity')
q.aggregate(Sum(F('price_sale') * F('quantity')), output_field=FloatField())
# falhou
''' ------------ '''
# Django 1.8.3
# http://stackoverflow.com/a/35076326/802542
from core.models import SaleDetail
from django.db.models import Sum, F, FloatField
q = SaleDetail.objects.filter(sale=1).values('price_sale', 'quantity')
q.aggregate(Sum(F('price_sale') * ('quantity'), output_field=FloatField()))
# falhou

''' ------------ '''
qs = SaleDetail.objects.filter(sale=1).values_list('price_sale', 'quantity')
list(map(lambda q: q[0] * q[1], qs))
# funciona no template, mas não funciona no Admin.

''' ------------ '''
# Django 1.7
# http://pt.stackoverflow.com/a/66694/761
from vendas_project.vendas.models import SaleDetail
from django.db.models import Sum
SaleDetail.objects.extra(
    select={'subtotal': 'round(price_sale * quantity, 2)',
            }).values('price_sale', 'quantity', 'subtotal').filter(sale=2)
SaleDetail.objects.extra(
    select={'total': 'round(sum(price_sale*quantity),2)', }).values('total').filter(sale=2)
# OK

''' ------------ '''
# Django 1.8
from vendas_project.vendas.models import SaleDetail
from django.db.models import Sum, F, FloatField
q = SaleDetail.objects.filter(sale=1).values('price_sale', 'quantity')
qs = q.annotate(
    subtotal=(F('price_sale') * F('quantity')),
    output_field=FloatField())
# Falhou

''' ------------ '''
# Django 1.8
from vendas_project.vendas.models import SaleDetail
from django.db.models import F, FloatField, ExpressionWrapper
q = SaleDetail.objects.filter(sale=1).values('price_sale', 'quantity')
qs = q.annotate(subtotal=ExpressionWrapper(
    F('price_sale') * F('quantity')), output_field=FloatField())
qs[0].subtotal
t = qs.aggregate(total=Sum('subtotal'))
t.total

'''
Copiando uma venda
'''
from vendas_project.vendas.models import Sale, SaleDetail

s = Sale.objects.filter(pk=300)  # filtra a Venda pelo pk
d = SaleDetail.objects.filter(sale=s)  # filtra os itens dessa Venda
s = Sale.objects.get(pk=s)  # com o get pega o pk da Venda que foi filtrada
s.pk = None
s.save()  # salva uma cópia da Venda
for i in d:
    n = SaleDetail.objects.create(
        sale=s, product=i.product, quantity=i.quantity, price_sale=i.price_sale)
