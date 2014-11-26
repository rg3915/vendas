#!python3
# -*- coding: utf-8 -*-
import io
import sys
import datetime
import names
from gen_random_values import *

lista = []
repeat = 50
with io.open('customer', 'wt') as f:
    for i in range(repeat):
        cpf = gen_cpf()
        fname = names.get_first_name()
        lname = names.get_last_name()
        email = fname[0].lower() + '.' + lname.lower() + '@email.com'
        phone = gen_phone()
        date = gen_timestamp() + '+00'
        # cpf, firstname, lastname, email, phone, created_at, modified_at
        lista.append((cpf, fname, lname, email, phone, date, date))
    for l in lista:
        s = "String INSERT INTO vendas_customer (cpf, firstname, lastname, email, phone, created_at, modified_at) VALUES ('" + l[0] + "','" + str(l[1]) + "','" + l[2] + "','" + l[
            3] + "','" + l[4] + "','" + l[5] + "','" + l[6] + "');\nKeyStrPress Return KeyStrRelease Return\n"
        f.write(str(s))
