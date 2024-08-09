from django import forms
from .models import Configuracoes

class ConfiguracoesForm(forms.ModelForm):
	class Meta:
		model = Configuracoes
		fields = ['aparencia_tela', 'notificacaoRecebimentos', 'diasNotificacaoReceb', 'notificacaoGastos', 'diasNotificacaoGastos', 'notificacaoContas', 'diasNotificacaoContas']

	def clean(self):
		cleaned_data = super().clean()

		notificacao_recebidos = cleaned_data.get('notificacaoRecebidos')
		dias_notificacao_receb = cleaned_data.get('diasNotificacaoReceb')

		notificacao_gastos = cleaned_data.get('notificacaoGastos')
		dias_notificacao_gastos = cleaned_data.get('diasNotificacaoGastos')

		notificacao_contas = cleaned_data.get('notificacaoContas')
		dias_notificacao_contas = cleaned_data.get('diasNotificacaoContas')

		if notificacao_recebidos and not dias_notificacao_receb:
				self.add_error('diasNotificacaoReceb', 'Este campo é obrigatório se a notificação de recebidos estiver ativada.')
		if not notificacao_recebidos and dias_notificacao_receb:
				self.add_error('diasNotificacaoReceb', 'Este campo deve estar vazio se a notificação de recebidos não estiver ativada.')

		if notificacao_gastos:
			if not dias_notificacao_gastos:
				self.add_error('diasNotificacaoGastos', 'Este campo é obrigatório se a notificação de gastos estiver ativada.')
		else:
			if dias_notificacao_gastos:
				self.add_error('diasNotificacaoGastos', 'Este campo deve estar vazio se a notificação de gastos não estiver ativada.')

		if notificacao_contas:
			if not dias_notificacao_contas:
				self.add_error('diasNotificacaoContas', 'Este campo é obrigatório se a notificação de contas estiver ativada.')
		else:
			if dias_notificacao_contas:
				self.add_error('diasNotificacaoContas', 'Este campo deve estar vazio se a notificação de contas não estiver ativada.')	

		return cleaned_data

