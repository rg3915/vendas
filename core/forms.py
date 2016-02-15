from django import forms
from .models import Sale, SaleDetail


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(forms.ModelForm):

    class Meta:
        model = SaleDetail
        fields = '__all__'
