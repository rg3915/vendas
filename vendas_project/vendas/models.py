# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format
import locale

locale.setlocale(locale.LC_ALL, '')


class Customer(models.Model):
    cpf = models.CharField(_('CPF'), max_length=11)
    firstname = models.CharField(_('Nome'), max_length=20)
    lastname = models.CharField(_('Sobrenome'), max_length=20)
    email = models.EmailField(_('e-mail'), unique=True)
    phone = models.CharField(_('Fone'), max_length=18)
    birthday = models.DateTimeField(_('Nascimento'))
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

    # vendas por cliente
    def get_sales_count(self):
        return self.customer_sale.count()


class Brand(models.Model):
    brand = models.CharField(_('Marca'), max_length=50, unique=True)

    class Meta:
        ordering = ['brand']
        verbose_name = u'marca'
        verbose_name_plural = u'marcas'

    def __unicode__(self):
        return self.brand


class Product(models.Model):
    imported = models.BooleanField(_('Importado'), default=False)
    outofline = models.BooleanField(_('Fora de linha'), default=False)
    ncm = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand)
    product = models.CharField(_('Produto'), max_length=30, unique=True)
    price = models.DecimalField(_('Preço'), max_digits=6, decimal_places=2)
    stoq = models.IntegerField(_('Estoque atual'))
    stoq_min = models.PositiveIntegerField(_('Estoque mínimo'), default=0)

    class Meta:
        ordering = ['product']
        verbose_name = u'produto'
        verbose_name_plural = u'produtos'

    def __unicode__(self):
        return self.product

    @property
    def get_price(self):
        return self.price


class Sale(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_sale')
    date_sale = models.DateTimeField(
        _('Data da venda'), auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(
        _('Modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = u'venda'
        verbose_name_plural = u'vendas'

    def __unicode__(self):
        return u"%d" % self.id + u"/%s" % self.date_sale.year
    codigo = property(__unicode__)

    def get_detalhe(self):
        return u"/sale/%i" % self.id

    def get_itens(self):
        return self.sales_det.count()

    def get_total(self):
        s = self.sales_det.aggregate(
            subtotal_sum=models.Sum('subtotal')).get('subtotal_sum') or 0
        return s


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField(_('quantidade'))
    price_sale = models.DecimalField(
        _('Preço de venda'), max_digits=6, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity or 0 * self.price_sale or 0.00
        super(SaleDetail, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.sale)

    def getID(self):
        return u"07%d" % self.id
