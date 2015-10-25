# -*- coding: utf-8 -*-
import rstr
import datetime
from random import random, randint, choice
from decimal import Decimal


def gen_age():
    # gera numeros inteiros entre 15 e 99
    return randint(15, 99)


def gen_cpf():
    # gera uma string com 11 caracteres numericos
    return rstr.rstr('1234567890', 11)


def gen_ncm():
    return rstr.rstr('123456789', 8)


def gen_phone():
    # gera um telefone no formato (xx) xxxx-xxxx
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))


def gen_timestamp(min_year=1980, max_year=1996):
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    min_date = datetime(min_year, 1, 1)
    max_date = datetime(max_year + 1, 1, 1)
    delta = random() * (max_date - min_date).total_seconds()
    return (min_date + timedelta(seconds=delta)).isoformat(" ")

''' sorteio que cai dia 29 de fevereiro
i,d=0,gen_timestamp()
while d[5:10] != '02-29' and i < 100000:
    i, d=i+1,gen_timestamp()

i,d
'''


def gen_decimal(max_digits, decimal_places):
    num_as_str = lambda x: ''.join(
        [str(randint(0, 9)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places),
                              num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']


def gen_ipi():
    num_as_str = lambda x: ''.join(
        [str(randint(0, 9)) for i in range(x)])
    return Decimal("0.%s" % (num_as_str(2)))


def gen_city():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Belém', 'PA'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiânia', 'GO'],
        [u'Salvador', 'BA'],
        [u'Guarulhos', 'SP'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Fortaleza', 'CE'],
        [u'São Luís', 'MA'],
        [u'Belo Horizonte', 'MG'],
        [u'São Gonçalo', 'RJ'],
        [u'Manaus', 'AM'],
        [u'Maceió', 'AL'],
        [u'Curitiba', 'PR'],
        [u'Duque de Caxias', 'RJ'],
        [u'Recife', 'PE'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return choice(list_city)
