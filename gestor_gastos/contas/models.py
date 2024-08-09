# aqui eh onde vamos definir as tabelas do banco de dados
from django.db import models

class Contas(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    origem = models.CharField(max_length=255)
    dataVencimento = models.DateField()
    TIPO_CONTA = [
        ('A', 'Aluguel'),
        ('G', 'Água'),
        ('L', 'Luz'),
        ('I', 'Internet'),
        ('O', 'Outros'),
    ]
    tipoConta = models.CharField(max_length=1, choices=TIPO_CONTA, blank=True, null=True)

    def __str__(self):
        return f"{self.origem} - {self.valor}"