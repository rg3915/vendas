#!python3
# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
from gen_random_values import *

lista = []
repeat = 900
with io.open('saledetail', 'wt') as f:
    for i in range(repeat):
        sale = random.randint(1, 222)
        product = random.randint(1, 51)
        quantity = random.randint(1, 100)
        price = generate_price()
        # sale_id, product_id, quantity, price_sale
        lista.append((sale, product, quantity, price))
    for l in lista:
        s = "String INSERT INTO vendas_saledetail (sale_id, product_id, quantity, price_sale) VALUES (" + str(
            l[0]) + "," + str(l[1]) + "," + str(l[2]) + "," + l[3] + ");\nKeyStrPress Return KeyStrRelease Return\n"
        f.write(str(s))
