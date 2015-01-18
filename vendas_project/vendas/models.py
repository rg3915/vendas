# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format


class Person(models.Model):

    """ Person is abstract model """
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
        abstract = True
        ordering = ['firstname']

    def __unicode__(self):
        return self.firstname + " " + self.lastname
    full_name = property(__unicode__)


class Customer(Person):
    pass

    class Meta:
        verbose_name = u'cliente'
        verbose_name_plural = u'clientes'

    # clica na pessoa e retorna as vendas dela
    def get_sale_customer_url(self):
        return u"/sale/?customer=%i" % self.id

    # vendas por pessoa
    def get_sales_count(self):
        return self.customer_sale.count()


class Seller(Person):
    active = models.BooleanField(_('ativo'), default=True)
    internal = models.BooleanField(_('interno'), default=True)
    commissioned = models.BooleanField(_('comissionado'), default=True)
    commission = models.DecimalField(
        _(u'comissão'), max_digits=6, decimal_places=2, default=0.01, blank=True)

    class Meta:
        verbose_name = u'vendedor'
        verbose_name_plural = u'vendedores'

    # clica na pessoa e retorna as vendas dela
    def get_sale_url(self):
        return u"/sale/?seller=%i" % self.id

    # vendas por pessoa
    def get_sales_count(self):
        return self.seller_sale.count()


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
    ncm = models.CharField(_('NCM'), max_length=8)
    brand = models.ForeignKey(Brand, verbose_name=_('marca'))
    product = models.CharField(_('Produto'), max_length=60, unique=True)
    price = models.DecimalField(_(u'Preço'), max_digits=6, decimal_places=2)
    ipi = models.DecimalField(
        _('IPI'), max_digits=3, decimal_places=2, blank=True)
    stock = models.IntegerField(_('Estoque atual'))
    stock_min = models.PositiveIntegerField(_(u'Estoque mínimo'), default=0)

    class Meta:
        ordering = ['product']
        verbose_name = u'produto'
        verbose_name_plural = u'produtos'

    def __unicode__(self):
        return self.product

    def get_price(self):
        return u"R$ %s" % number_format(self.price, 2)

    def get_ipi(self):
        return u"%s" % number_format(self.ipi * 100, 0)


class Sale(models.Model):
    customer = models.ForeignKey(
        'Customer', related_name='customer_sale', verbose_name=_('cliente'))
    seller = models.ForeignKey(
        'Seller', related_name='seller_sale', verbose_name=_('vendedor'))
    date_sale = models.DateTimeField(
        _('Data da venda'), auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(
        _('Modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = u'venda'
        verbose_name_plural = u'vendas'

    def __unicode__(self):
        return u"%03d" % self.id + u"/%s" % self.date_sale.strftime('%y')
    codigo = property(__unicode__)

    def get_detalhe(self):
        return u"/sale/%i" % self.id

    # conta os itens em cada venda
    def get_itens(self):
        return self.sales_det.count()

    def get_total(self):
        s = self.sales_det.aggregate(
            subtotal_sum=models.Sum('subtotal')).get('subtotal_sum') or 0
        return u"R$ %s" % number_format(s, 2)


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(
        Product, related_name='product_det', verbose_name=_('produto'))
    quantity = models.PositiveSmallIntegerField(_('quantidade'))
    price_sale = models.DecimalField(
        _(u'Preço de venda'), max_digits=6, decimal_places=2, default=0)
    ipi_sale = models.DecimalField(
        _(u'IPI'), max_digits=3, decimal_places=2, default=0.1)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity or 0 * self.price_sale or 0.00
        super(SaleDetail, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.sale)

    def getID(self):
        return u"%04d" % self.id

    def price_sale_formated(self):
        return u"R$ %s" % number_format(self.price_sale, 2)

    def get_ipi(self):
        return u"%s" % number_format(self.ipi_sale * 100, 0)

    def subtotal_formated(self):
        return u"R$ %s" % number_format(self.subtotal, 2)
