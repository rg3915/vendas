# -*- coding: utf-8 -*-

"""
    Este App gerencia um banco de dados sqlite3.
    Pode-se usar o modo interativo com python2.

    Popula as tabelas do banco de dados com valores randômicos.
    Banco de dados: 'db.sqlite3'
    Tabelas: 'vendas_brand',
             'vendas_customer',
             'vendas_product',
             'vendas_sale',
             'vendas_saledetail'
"""

import os
import io
import sqlite3
import random
import datetime
import names    # gera nomes randomicos
import rstr     # gera strings randomicas
from decimal import Decimal
from gen_random_values import gen_doc, gen_ncm, gen_phone, gen_decimal, gen_ipi, gen_timestamp

qcustomers = 60
qsellers = 20
qproducts = 1645  # 100
qsales = 300
qsaledetails = 1200


class Connect(object):

    ''' A classe Connect representa o banco de dados. '''

    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo nome do banco
            print("Banco:", db_name)
            # lendo a versão do banco
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            # imprimindo a versão do banco
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


class VendasDb(object):

    def __init__(self):
        self.db = Connect('../db.sqlite3')

    def insert_for_file(self):
        try:
            with open('brand.sql', 'rt') as f:
                dados = f.read()
                self.db.cursor.executescript(dados)
            print("Registros criados com sucesso na tabela vendas_brand.")
        except sqlite3.IntegrityError:
            print("Aviso: A marca deve ser única.")
            return False

    def insert_random_customer(self, repeat=qcustomers):
        ''' Inserir registros com valores randomicos '''

        customer_list = []
        for _ in range(repeat):
            # d = datetime.datetime.now().isoformat(" ")
            d = gen_timestamp(2014, 2015) + '+00'
            fname = names.get_first_name()
            lname = names.get_last_name()
            email = fname[0].lower() + '.' + lname.lower() + '@example.com'
            birthday = gen_timestamp() + '+00'
            customer_list.append(
                (gen_cpf(), fname, lname, email, gen_phone(), birthday, d, d))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_customer (cpf, firstname, lastname, email, phone, birthday, created, modified)
            VALUES (?,?,?,?,?,?,?,?)
            """, customer_list)
            self.db.commit_db()
            print("Inserindo %s registros na tabela vendas_customer." % repeat)
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def insert_random_seller(self, repeat=qsellers):
        ''' Inserir registros com valores randomicos '''

        seller_list = []
        for _ in range(repeat):
            d = gen_timestamp(2014, 2015) + '+00'
            fname = names.get_first_name()
            lname = names.get_last_name()
            email = fname[0].lower() + '.' + lname.lower() + '@example.com'
            birthday = gen_timestamp() + '+00'
            active = rstr.rstr('01', 1)
            internal = rstr.rstr('01', 1)
            commissioned = rstr.rstr('01', 1)
            commission = 0.01
            seller_list.append(
                (gen_doc(), fname, lname, email, gen_phone(), birthday, active, internal, commissioned, commission, d, d))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_seller (cpf, firstname, lastname, email, phone, birthday, active, internal, commissioned, commission, created, modified)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """, seller_list)
            self.db.commit_db()
            print("Inserindo %s registros na tabela vendas_seller." % repeat)
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def insert_random_product(self, repeat=qproducts):
        product_list = []
        for i in range(repeat):
            imported = rstr.rstr('01', 1)
            # escolha personalizada de produtos fora de linha
            if i % 26 == 0:
                if i > 0:
                    outofline = '1'
                else:
                    outofline = '0'
            else:
                outofline = '0'

            ncm = gen_ncm()
            brand = random.randint(1, 20)
            price = float(gen_decimal(4, 2))

            ipi = 0

            if imported == '1':
                ipi = float(gen_ipi())
                if ipi > 0.5:
                    ipi = ipi - 0.5

            stock = random.randint(1, 999)
            stock_min = random.randint(1, 20)

            f = io.open('products.txt', 'rt', encoding='utf-8')
            linelist = f.readlines()

            product = linelist[i].split(',')[0]
            product_list.append(
                (imported, outofline, ncm, brand, product, price, ipi, stock, stock_min))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_product (imported, outofline, ncm, brand_id, product, price, ipi, stock, stock_min)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, product_list)
            self.db.commit_db()
            print("Inserindo %s registros na tabela vendas_product." % repeat)
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O produto deve ser único.")
            return False

    def insert_random_sale(self, repeat=qsales):

        sale_list = []
        for _ in range(repeat):
            d = gen_timestamp(2014, 2015) + '+00'
            customer = random.randint(1, qcustomers)
            seller = random.randint(1, qsellers)
            sale_list.append((customer, seller, d, d))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_sale (customer_id, seller_id, date_sale, modified)
            VALUES (?,?,?,?)
            """, sale_list)
            self.db.commit_db()
            print("Inserindo %s registros na tabela vendas_sale." % repeat)
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            return False

    def insert_random_saledetail(self, repeat=qsaledetails):

        saledetail_list = []
        for _ in range(repeat):
            sale = random.randint(1, qsales)
            product = random.randint(1, qproducts)
            quantity = random.randint(1, 50)

            # find price and ipi of product
            r = self.db.cursor.execute(
                'SELECT price, ipi FROM vendas_product WHERE id = ?', (product,))
            v = r.fetchall()[0]
            price = v[0]
            ipi = v[1]

            subtotal = quantity * float(price)
            saledetail_list.append(
                (sale, product, quantity, price, ipi, subtotal))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_saledetail (sale_id, product_id, quantity, price_sale, ipi_sale, subtotal)
            VALUES (?,?,?,?,?,?)
            """, saledetail_list)
            self.db.commit_db()
            print("Inserindo %s registros na tabela vendas_saledetail." %
                  repeat)
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            return False

    def close_connection(self):
        self.db.close_db()

if __name__ == '__main__':
    v = VendasDb()
    v.insert_for_file()
    v.insert_random_customer()
    v.insert_random_seller()
    v.insert_random_product()  # 100
    v.insert_random_sale()
    v.insert_random_saledetail()
    v.close_connection()
    # repare que o valor do parâmetro pode ser mudado
