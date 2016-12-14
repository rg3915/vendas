from random import randint
import csv
from vendas.core.models import Product, Brand
from fixtures.gen_random_values import *

product_list = []

''' Lendo os dados de products_.csv '''
with open('fixtures/products_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        product_list.append(dct)
    f.close()

REPEAT = len(product_list) - 1600

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
    product = product_list[i]['product']
    price = float(gen_decimal(4, 2))
    ipi = 0
    if imported == 1:
        ipi = float(gen_ipi())
        if ipi > 0.5:
            ipi = ipi - 0.5
    stock = randint(1, 999)
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
    obj.save()


print('%d Produtos salvo com sucesso.' % REPEAT)
