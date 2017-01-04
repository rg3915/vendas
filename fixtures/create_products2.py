import csv
from random import randint
from django.db import IntegrityError
from vendas.core.models import Product, Brand
from fixtures.gen_random_values import *

# Pegar 5 produtos de cada categoria

product_list = []
CAT_MAX = 28  # Quant de Categorias. Sujeita a alteração

''' Lendo os dados de produtos.csv '''
for i in range(1, CAT_MAX):
    with open('fixtures/csv/produtos.csv', 'r') as f:
        r = csv.DictReader(f)
        for dct in r:
            product_list.append(dct)
        f.close()

REPEAT = len(product_list)
items_save_count = 0

for i in range(REPEAT):
    imported = randint(0, 1)
    # escolha personalizada de produtos fora de linha
    if i % 26 == 0:
        if i > 0:
            outofline = 1
        else:
            outofline = 0
    else:
        outofline = 0
    ncm = gen_ncm()
    b = randint(1, 20)
    brand = Brand.objects.get(pk=b)
    product = product_list[i]['title']
    price = float(product_list[i]['price'])
    ipi = 0
    if imported == 1:
        ipi = float(gen_ipi())
        if ipi > 0.5:
            ipi = ipi - 0.5
    stock = product_list[i]['available_quantity']
    stock_min = randint(1, 20)
    obj = Product(
        imported=imported,
        outofline=outofline,
        ncm=ncm,
        brand=brand,
        product=product,
        price=price,
        ipi=ipi,
        stock=stock,
        stock_min=stock_min,
    )
    try:
        obj.save()
        items_save_count += 1
    except IntegrityError:
        print('Registro existente.')

print('%d Produtos salvo com sucesso.' % items_save_count)
