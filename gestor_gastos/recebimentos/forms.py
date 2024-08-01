from django import forms
from .models import Recebimentos

class RecebimentoForm(forms.ModelForm):
    class Meta:
        model = Recebimentos
        fields = ['valor', 'origem', 'tipo', 'data', 'repeticao']
