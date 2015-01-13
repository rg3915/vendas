# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(unique=True, max_length=50, verbose_name='Marca')),
            ],
            options={
                'ordering': ['brand'],
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('firstname', models.CharField(max_length=20, verbose_name='Nome')),
                ('lastname', models.CharField(max_length=20, verbose_name='Sobrenome')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=18, verbose_name='Fone')),
                ('birthday', models.DateTimeField(verbose_name='Nascimento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'ordering': ['firstname'],
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imported', models.BooleanField(default=False, verbose_name='Importado')),
                ('outofline', models.BooleanField(default=False, verbose_name='Fora de linha')),
                ('ncm', models.CharField(max_length=8)),
                ('product', models.CharField(unique=True, max_length=60, verbose_name='Produto')),
                ('price', models.DecimalField(verbose_name='Pre\xe7o', max_digits=6, decimal_places=2)),
                ('stoq', models.IntegerField(verbose_name='Estoque atual')),
                ('stoq_min', models.PositiveIntegerField(default=0, verbose_name='Estoque m\xednimo')),
                ('brand', models.ForeignKey(verbose_name='marca', to='vendas.Brand')),
            ],
            options={
                'ordering': ['product'],
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_sale', models.DateTimeField(auto_now_add=True, verbose_name='Data da venda')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('customer', models.ForeignKey(related_name=b'customer_sale', verbose_name='cliente', to='vendas.Customer')),
            ],
            options={
                'verbose_name': 'venda',
                'verbose_name_plural': 'vendas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='quantidade')),
                ('price_sale', models.DecimalField(default=0, verbose_name='Pre\xe7o de venda', max_digits=6, decimal_places=2)),
                ('subtotal', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('product', models.ForeignKey(related_name=b'product_det', verbose_name='produto', to='vendas.Product')),
                ('sale', models.ForeignKey(related_name=b'sales_det', to='vendas.Sale')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
