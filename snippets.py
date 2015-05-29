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
qs = SaleDetail.objects.filter(sale=1).values_list('price_sale', 'quantity')
list(map(lambda q: q[0] * q[1], qs))
# funciona no template, mas não funciona no Admin.


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
