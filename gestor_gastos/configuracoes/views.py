from django.shortcuts import render, redirect
from .models import Configuracoes
from .forms import ConfiguracoesForm
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def configuracoes(request):
	if request.method == 'POST':
		form = ConfiguracoesForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			form.save()
			print("Formulário válido e salvo com sucesso!")
			return redirect('configuracoes')  
		else:
			print("Formulário inválido: ", form.errors)
	else:
		form = ConfiguracoesForm()
	
	context = {'form': form}
	return render(request, 'pag_configuracoes.html', context)


