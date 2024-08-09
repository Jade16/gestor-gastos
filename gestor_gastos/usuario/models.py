from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms   

def tamanho_img(image):
    max_size_kb = 512  # Tamanho máximo da imagem em KB (por exemplo, 512 KB)
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"O tamanho da imagem não pode exceder {max_size_kb} KB.")

class Usuario(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Use um related_name exclusivo
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',  # Use um related_name exclusivo
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    fotoPerfil = models.ImageField(upload_to='imagens/usuario.svg', validators=[tamanho_img], null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    # senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     senha = cleaned_data.get('senha')
    #     confirmar_senha = cleaned_data.get('confirmar_senha')

    #     if senha and confirmar_senha and senha != confirmar_senha:
    #         self.add_error('confirmar_senha', 'As senhas não coincidem.')

    #     return cleaned_data
    pass

    def __str__(self):
        return f"{self.origem} - {self.valor}"