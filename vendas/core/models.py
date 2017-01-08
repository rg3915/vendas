from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.formats import number_format

gender_list = [('M', 'masculino'), ('F', 'feminino')]


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):

    """ Person is abstract model """
    gender = models.CharField('gênero', max_length=1, choices=gender_list)
    cpf = models.CharField('CPF', max_length=11)
    firstname = models.CharField('Nome', max_length=20)
    lastname = models.CharField('Sobrenome', max_length=20)
    email = models.EmailField('e-mail', unique=True)
    phone = models.CharField('Fone', max_length=18)
    birthday = models.DateTimeField('Nascimento')

    class Meta:
        abstract = True
        ordering = ['firstname']

    def __str__(self):
        return self.firstname + " " + self.lastname
    full_name = property(__str__)


class Customer(Person):
    pass

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    # clica na pessoa e retorna os detalhes dela
    def get_customer_url(self):
        return "/customer/%i" % self.id

    # clica em vendas e retorna as vendas da pessoa
    def get_sale_customer_url(self):
        return "/sale/?customer=%i" % self.id

    # vendas por pessoa
    def get_sales_count(self):
        return self.customer_sale.count()


class Seller(Person):
    active = models.BooleanField('ativo', default=True)
    internal = models.BooleanField('interno', default=True)
    commissioned = models.BooleanField('comissionado', default=True)
    commission = models.DecimalField(
        'comissão', max_digits=6, decimal_places=2, default=0.01, blank=True)

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    # clica no vendedor e retorna os detalhes dele
    def get_seller_url(self):
        return "/seller/%i" % self.id

    # clica em vendas e retorna as vendas do vendedor
    def get_sale_seller_url(self):
        return "/sale/?seller=%i" % self.id

    # vendas por pessoa
    def get_sales_count(self):
        return self.seller_sale.count()

    def get_commission(self):
        return "%s" % number_format(self.commission * 100, 0)


class Brand(models.Model):
    brand = models.CharField('Marca', max_length=50, unique=True)

    class Meta:
        ordering = ['brand']
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.brand


class Category(models.Model):
    id = models.CharField('Id', max_length=7, primary_key=True)
    category = models.CharField('Categoria', max_length=50, unique=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category


class Product(models.Model):
    imported = models.BooleanField('Importado', default=False)
    outofline = models.BooleanField('Fora de linha', default=False)
    ncm = models.CharField('NCM', max_length=8)
    brand = models.ForeignKey(Brand, verbose_name='marca')
    product = models.CharField('Produto', max_length=100, unique=True)
    price = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    ipi = models.DecimalField(
        'IPI', max_digits=3, decimal_places=2, blank=True)
    stock = models.IntegerField('Estoque atual')
    stock_min = models.PositiveIntegerField('Estoque mínimo', default=0)
    category = models.ForeignKey(Category, verbose_name='categoria',
                                 null=True, blank=True)

    class Meta:
        ordering = ['product']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.product

    def get_price(self):
        return "R$ %s" % number_format(self.price, 2)

    def get_ipi(self):
        return "%s" % number_format(self.ipi * 100, 0)


class Sale(TimeStampedModel):
    customer = models.ForeignKey(
        'Customer', related_name='customer_sale', verbose_name='cliente')
    seller = models.ForeignKey(
        'Seller', related_name='seller_sale', verbose_name='vendedor')

    class Meta:
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        return "%03d" % self.id + "/%s" % self.created.strftime('%y')
    codigo = property(__str__)

    def get_absolute_url(self):
        return reverse_lazy('core:sale_detail', pk=self.pk)

    def get_detalhe(self):
        return "/sale/%i" % self.id

    # conta os itens em cada venda
    def get_itens(self):
        return self.sales_det.count()

    def get_total(self):
        qs = self.sales_det.filter(sale=self.pk).values_list(
            'price_sale', 'quantity') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0] * q[1], qs))
        return "R$ %s" % number_format(t, 2)


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(
        Product, related_name='product_det', verbose_name='produto')
    quantity = models.PositiveSmallIntegerField('quantidade')
    price_sale = models.DecimalField(
        'Preço de venda', max_digits=6, decimal_places=2, default=0)
    ipi_sale = models.DecimalField(
        'IPI', max_digits=3, decimal_places=2, default=0.1)

    def __str__(self):
        return str(self.sale)

    def get_subtotal(self):
        return self.price_sale * (self.quantity or 0)

    subtotal = property(get_subtotal)

    def getID(self):
        return "%04d" % self.id

    def price_sale_formated(self):
        return "R$ %s" % number_format(self.price_sale, 2)

    def get_ipi(self):
        return "%s" % number_format(self.ipi_sale * 100, 0)

    def subtotal_formated(self):
        return "R$ %s" % number_format(self.subtotal, 2)
