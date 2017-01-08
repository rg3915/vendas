import csv
from random import randint
from django.db import IntegrityError
from vendas.core.models import Product, Brand, Category
from fixtures.gen_random_values import *

product_list = []
# Quant de Categorias
CAT_MAX = sum(1 for line in open('fixtures/csv/categorias.csv'))

''' Lendo os dados de produtos.csv '''
for i in range(1, CAT_MAX):
    with open('fixtures/csv/produtos.csv', 'r') as f:
        r = csv.DictReader(f)
        for dct in r:
            product_list.append(dct)
        f.close()


REPEAT = len(product_list)
items_save_count = 0


def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not n % i:
                return False
    else:
        return False
    return True


for i in range(REPEAT):
    imported = randint(0, 1)
    # Todos produtos cujo id é primo são produtos fora de linha
    if is_prime(i):
        outofline = 1
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
    category_id = product_list[i]['category_id']
    category = Category.objects.get(pk=category_id)
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
        category=category,
    )
    try:
        obj.save()
        items_save_count += 1
    except IntegrityError:
        print('Registro existente.')


print('%d Produtos salvo com sucesso.' % items_save_count)
