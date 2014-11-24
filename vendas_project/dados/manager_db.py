# -*- coding: utf-8 -*-

"""
    Este App gerencia um banco de dados sqlite3.
    Pode-se usar o modo interativo com python2.
    
    Popula as tabelas do banco de dados com valores randômicos.
    Banco de dados: 'db.sqlite3'
    Tabelas: 'vendas_category',
             'vendas_customer',
             'vendas_product',
             'vendas_sale',
             'vendas_saledetail'
"""

import os
import sqlite3
import random
import datetime
import names    # gera nomes randomicos, only python <= 3.3
import rstr     # gera strings randomicas

qcustomers = 50
qproducts = 100
qsales = 200
qsaledetails = 1000


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
            with open('dados.sql', 'rt') as f:
                dados = f.read()
                self.db.cursor.executescript(dados)
            print("Registros criados com sucesso na tabela vendas_category.")
        except sqlite3.IntegrityError:
            print("Aviso: A categoria deve ser única.")
            return False

    def generate_cpf(self):
        return rstr.rstr('1234567890', 11)

    def generate_phone(self):
        return '({0}) {1}-{2}'.format(
            rstr.rstr('1234567890', 2),
            rstr.rstr('1234567890', 4),
            rstr.rstr('1234567890', 4))

    def insert_random_customer(self, repeat=qcustomers):
        ''' Inserir registros com valores randomicos
        names só funciona no python <= 3.3 '''

        customer_list = []
        for _ in range(repeat):
            d = datetime.datetime.now().isoformat(" ")
            fname = names.get_first_name()
            lname = names.get_last_name()
            email = fname[0].lower() + '.' + lname.lower() + '@example.com'
            customer_list.append(
                (self.generate_cpf(), fname, lname, email, self.generate_phone(), d, d))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_customer (cpf, firstname, lastname, email, phone, created_at, modified_at)
            VALUES (?,?,?,?,?,?,?)
            """, customer_list)
            self.db.commit_db()
            print("Inserindo %s registros na tabela vendas_customer." % repeat)
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def generate_price(self):
        return '{0}.{1}'.format(rstr.rstr('1234567890', 2, 4), rstr.rstr('1234567890', 2))

    def insert_random_product(self, repeat=qproducts):

        product_list = []
        for i in range(repeat):
            imported = rstr.rstr('01', 1)
            outofline = rstr.rstr('01', 1)
            category = random.randint(1, 23)
            product = 'SKU' + str(i)
            if i < 10:
                product = 'SKU0' + str(i)
            product_list.append(
                (imported, outofline, category, product, self.generate_price()))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_product (imported, outofline, category_id, product, price)
            VALUES (?,?,?,?,?)
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
            d = datetime.datetime.now().isoformat(" ")
            customer = random.randint(1, qcustomers)
            sale_list.append((customer, d, d))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_sale (customer_id, date_sale, modified_at)
            VALUES (?,?,?)
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
            quantity = random.randint(1, 100)
            saledetail_list.append(
                (sale, product, quantity, self.generate_price()))
        try:
            self.db.cursor.executemany("""
            INSERT INTO vendas_saledetail (sale_id, product_id, quantity, price_sale)
            VALUES (?,?,?,?)
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
    v.insert_random_customer(60)
    v.insert_random_product(120)
    v.insert_random_sale(224)
    v.insert_random_saledetail(900)
    v.close_connection()
    # repare que o valor do parâmetro pode ser mudado
