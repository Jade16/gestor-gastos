# aqui eh onde vamos definir as tabelas do banco de dados
from django.db import models


class Configuracoes(models.Model):
	# configuracoes gerais
	APARENCIA = [
		('C', 'Claro'),
		('E', 'Escuro'),
	]
	aparencia_tela = models.CharField(max_length=1, choices=APARENCIA, blank=True, null=True, default='C')

	# configuracoes recebimentos
	notificacaoRecebimentos = models.BooleanField(default=False)
	diasNotificacaoReceb = models.IntegerField()

	# configuracoes gastos
	notificacaoGastos = models.BooleanField(default=False)
	PERIODO = [
		('1', 'Uma vez por dia'),
		('2', 'A cada dois dias'),
		('3', 'Uma vez por semana'),
		('4', 'Uma vez a cada duas semanas'),
		('5', 'Uma vez a cada quinzena'),
		('6', 'Uma vez por mês'),
	]
	diasNotificacaoGastos = models.CharField(max_length=1, choices=PERIODO, blank=True, null=True)

	# configuracoes contas
	notificacaoContas = models.BooleanField(default=False)
	diasNotificacaoContas = models.IntegerField()