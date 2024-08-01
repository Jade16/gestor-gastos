# aqui eh onde vamos definir as tabelas do banco de dados
from django.db import models

class Gastos(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    origem = models.CharField(max_length=255)
    TIPO_CHOICES = [
        ('A', 'Alimentação'),
        ('S', 'Saúde'),
        ('L', 'Laser'),
        ('T', 'Transporte'),
        ('H', 'Higiene'),        
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data = models.DateField()
    descricao = # nao sei
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