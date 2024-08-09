from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError

class UsuarioForm(forms.ModelForm):
	senha = forms.CharField(widget=forms.PasswordInput, label="senha")
	confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")
	
	class Meta:
		model = Usuario
		fields = ['fotoPerfil', 'email']

	def clean_confirmar_senha(self):
		senha = self.cleaned_data.get('senha')
		confirmar_senha = self.cleaned_data.get('confirmar_senha')
		if senha and confirmar_senha and senha != confirmar_senha:
			raise ValidationError("As senhas não coincidem.")
		return confirmar_senha

	def save(self, commit=True):
		Usuario = super(UsuarioForm, self).save(commit=False)
		Usuario.set_password(self.cleaned_data["senha"])
		if commit:
			Usuario.save()
		return Usuario