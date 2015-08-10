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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('brand', models.CharField(max_length=50, verbose_name='Marca', unique=True)),
            ],
            options={
                'verbose_name_plural': 'marcas',
                'ordering': ['brand'],
                'verbose_name': 'marca',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('firstname', models.CharField(max_length=20, verbose_name='Nome')),
                ('lastname', models.CharField(max_length=20, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail', unique=True)),
                ('phone', models.CharField(max_length=18, verbose_name='Fone')),
                ('birthday', models.DateTimeField(verbose_name='Nascimento')),
            ],
            options={
                'verbose_name_plural': 'clientes',
                'verbose_name': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('imported', models.BooleanField(default=False, verbose_name='Importado')),
                ('outofline', models.BooleanField(default=False, verbose_name='Fora de linha')),
                ('ncm', models.CharField(max_length=8, verbose_name='NCM')),
                ('product', models.CharField(max_length=60, verbose_name='Produto', unique=True)),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Preço', max_digits=6)),
                ('ipi', models.DecimalField(blank=True, decimal_places=2, verbose_name='IPI', max_digits=3)),
                ('stock', models.IntegerField(verbose_name='Estoque atual')),
                ('stock_min', models.PositiveIntegerField(default=0, verbose_name='Estoque mínimo')),
                ('brand', models.ForeignKey(to='core.Brand', verbose_name='marca')),
            ],
            options={
                'verbose_name_plural': 'produtos',
                'ordering': ['product'],
                'verbose_name': 'produto',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('customer', models.ForeignKey(related_name='customer_sale', verbose_name='cliente', to='core.Customer')),
            ],
            options={
                'verbose_name_plural': 'vendas',
                'verbose_name': 'venda',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='quantidade')),
                ('price_sale', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Preço de venda')),
                ('ipi_sale', models.DecimalField(decimal_places=2, default=0.1, max_digits=3, verbose_name='IPI')),
                ('product', models.ForeignKey(related_name='product_det', verbose_name='produto', to='core.Product')),
                ('sale', models.ForeignKey(related_name='sales_det', to='core.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('firstname', models.CharField(max_length=20, verbose_name='Nome')),
                ('lastname', models.CharField(max_length=20, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail', unique=True)),
                ('phone', models.CharField(max_length=18, verbose_name='Fone')),
                ('birthday', models.DateTimeField(verbose_name='Nascimento')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('internal', models.BooleanField(default=True, verbose_name='interno')),
                ('commissioned', models.BooleanField(default=True, verbose_name='comissionado')),
                ('commission', models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=6, verbose_name='comissão')),
            ],
            options={
                'verbose_name_plural': 'vendedores',
                'verbose_name': 'vendedor',
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='seller',
            field=models.ForeignKey(related_name='seller_sale', verbose_name='vendedor', to='core.Seller'),
        ),
    ]
