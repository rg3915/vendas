# -*- coding: utf-8 -*-
from django import forms
from models import Customer, Sale


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
