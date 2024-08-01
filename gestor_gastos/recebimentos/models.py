# aqui eh onde vamos definir as tabelas do banco de dados
from django.db import models

class Recebimentos(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    origem = models.CharField(max_length=255)
    TIPO_CHOICES = [
        ('F', 'Fixo'),
        ('V', 'Variável'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data = models.DateField()
    REPETICAO_CHOICES = [
        ('Q', 'Quinzenal'),
        ('S', 'Semanal'),
        ('M', 'Mensal'),
        # ('A', 'Anual'),
        ('N', 'Não se repete'),
    ]
    repeticao = models.CharField(max_length=1, choices=REPETICAO_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.origem} - {self.valor}"