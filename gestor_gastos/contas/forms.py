from django import forms
from .models import Contas

class ContaForm(forms.ModelForm):
    class Meta:
        model = Contas
        fields = ['valor', 'origem', 'dataVencimento', 'tipoConta']
