# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class Cliente(models.Model):
    cpf = models.CharField('CPF', max_length=11)
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    email = models.CharField('e-mail', max_length=50)
    fone = models.CharField('Fone', max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True, auto_now=False)
    modificado_em = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = u'cliente'
        verbose_name_plural = u'clientes'

    def __unicode__(self):
        return self.nome + " " + self.sobrenome


class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=50)

    class Meta:
        verbose_name = u'categoria'
        verbose_name_plural = u'categorias'

    def __unicode__(self):
        return self.categoria


class Produto(models.Model):

    def url(self, filename):
        caminho = "static/produto/%s/%s" % (self.produto, str(filename))
        return caminho

    importado = models.BooleanField('Importado', default=False)
    foradelinha = models.BooleanField('Fora de linha', default=False)
    categoria = models.ForeignKey(Categoria)
    produto = models.CharField('Produto', max_length=50)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    imagem = models.ImageField('Imagem', upload_to=url, null=True, blank=True)

    class Meta:
        verbose_name = u'produto'
        verbose_name_plural = u'produtos'

    def __unicode__(self):
        return self.produto


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente)
    datavenda = models.DateTimeField(
        'Data da venda', auto_now_add=True, auto_now=False)
    modificado_em = models.DateTimeField(auto_now_add=False, auto_now=True)
    preco = models.DecimalField(
        'Preço', default='12.75', max_digits=8, decimal_places=2)

    def __unicode__(self):
        return unicode(self.datavenda)

    def _get_total(self):
        soma = 0

        for det_venda in self.det_vendas.all():
            soma += det_venda.subtotal

        return soma
    total = property(_get_total)


class DetVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='det_vendas')
    produto = models.ForeignKey(Produto)
    quantidade = models.IntegerField()
    precovenda = models.DecimalField(
        'Preço de venda', default='produto.preco', max_digits=8, decimal_places=2)

    def __unicode__(self):
        return unicode(self.venda)

    def _get_subtotal(self):
        if self.quantidade:
            return self.precovenda * self.quantidade
    subtotal = property(_get_subtotal)
