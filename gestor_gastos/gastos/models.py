# aqui eh onde vamos definir as tabelas do banco de dados
from django.db import models

class Gastos(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    origem = models.CharField(max_length=255)
    data = models.DateField()
    TIPO_CHOICES = [
        ('M', 'Mercado'),
        ('S', 'Saúde'),
        ('L', 'Laser'),
        ('T', 'Transporte'),
        ('A', 'Alimentação'),        
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    descricao = models.TextField(max_length=500)
    PAGAMENTO = [
        ('D', 'Débito'),
        ('C', 'Crédito'),
    ]
    tipoPagamento = models.CharField(max_length=1, choices=PAGAMENTO)
    parcelas = models.IntegerField()
    
    def __str__(self):
        return f"{self.origem} - {self.valor}"