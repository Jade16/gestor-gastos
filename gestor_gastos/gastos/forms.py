from django import forms
from .models import Gastos

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['valor', 'origem', 'data', 'tipo', 'descricao', 'parcelas']
