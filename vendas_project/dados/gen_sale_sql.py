#!python3
# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
from gen_random_values import *

lista = []
repeat = 224
with io.open('sale', 'wt') as f:
    for i in range(repeat):
        customer = random.randint(1, 52)
        date = gen_timestamp() + '+00'
        d = datetime.datetime.now().isoformat(" ") + '+00'
        # customer_id, date_sale, modified_at
        lista.append((customer, date, d))
    for l in lista:
        s = "String INSERT INTO vendas_sale (customer_id, date_sale, modified_at) VALUES (" + str(
            l[0]) + ",'" + l[1] + "','" + l[2] + "');\nKeyStrPress Return KeyStrRelease Return\n"
        f.write(str(s))
