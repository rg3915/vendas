# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format
import locale

locale.setlocale(locale.LC_ALL, '')


class Customer(models.Model):
    cpf = models.CharField(_('CPF'), max_length=11)
    firstname = models.CharField(_('Nome'), max_length=50)
    lastname = models.CharField(_('Sobrenome'), max_length=50)
    email = models.CharField(_('e-mail'), max_length=50, unique=True)
    phone = models.CharField(_('Fone'), max_length=50)
    created_at = models.DateTimeField(
        _('Criado em'), auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(
        _('Modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['firstname']
        verbose_name = u'cliente'
        verbose_name_plural = u'clientes'

    def __unicode__(self):
        return self.firstname + " " + self.lastname
    full_name = property(__unicode__)


class Category(models.Model):
    category = models.CharField(_('Categoria'), max_length=50, unique=True)

    class Meta:
        ordering = ['category']
        verbose_name = u'categoria'
        verbose_name_plural = u'categorias'

    def __unicode__(self):
        return self.category


class Product(models.Model):
    imported = models.BooleanField(_('Importado'), default=False)
    outofline = models.BooleanField(_('Fora de linha'), default=False)
    category = models.ForeignKey(Category)
    product = models.CharField(_('Produto'), max_length=50, unique=True)
    price = models.DecimalField(_('Preço'), max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['product']
        verbose_name = u'produto'
        verbose_name_plural = u'produtos'

    def __unicode__(self):
        return self.product

    @property
    def get_price(self):
        return self.price

    def price_formated(self):
        if self.price != None:
            return locale.currency(self.price, grouping=True)
        return ''

    price_formated = property(price_formated)


class Sale(models.Model):
    customer = models.ForeignKey(Customer)
    date_sale = models.DateTimeField(
        _('Data da venda'), auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(
        _('Modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = u'venda'
        verbose_name_plural = u'vendas'

    def __unicode__(self):
        return unicode(self.date_sale)

    def _get_total(self):
        s = 0

        for sale_det in self.sales_det.all():
            s += sale_det.subtotal

        if s != None:
            return locale.currency(s, grouping=True)
        return ''
    total = property(_get_total)


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(_('quantidade'))
    price_sale = models.DecimalField(
        _('Preço de venda'), default=0, max_digits=8, decimal_places=2)

    def __unicode__(self):
        return unicode(self.sale)

    def _get_subtotal(self):
        if self.quantity:
            return self.price_sale * self.quantity
    subtotal = property(_get_subtotal)
