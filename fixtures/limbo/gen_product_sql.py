#!python3
# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
from gen_random_values import *

lista = []
repeat = 51
with io.open('product', 'wt') as f:
    for i in range(repeat):
        imported = rstr.rstr('01', 1)
        brand = random.randint(1, 23)
        product = 'SKU' + str(i)
        if i < 10:
            product = 'SKU0' + str(i)
        price = generate_price()
        # imported, outofline, brand_id, product, price
        lista.append((imported, brand, product, price))
    for l in lista:
        s = "String INSERT INTO vendas_product (imported, outofline, brand_id, product, price) VALUES (" + l[
            0] + ",1," + str(l[1]) + ",'" + l[2] + "'," + l[3] + ");\nKeyStrPress Return KeyStrRelease Return\n"
        f.write(str(s))
