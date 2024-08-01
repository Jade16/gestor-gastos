from django.shortcuts import render, redirect
from .models import Recebimentos
from .forms import RecebimentoForm
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def recebimentos(request):
	if request.method == 'POST':
		print("Recebendo POST request")
		form = RecebimentoForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			form.save()
			print("Formulário válido e salvo com sucesso!")
			return redirect('listar_recebimentos')  # Redirecionar para a lista de recebimentos
		else:
			print("Formulário inválido: ", form.errors)
	else:
		form = RecebimentoForm()
	
	context = {'form': form}
	return render(request, 'pag_recebimentos.html', context)

def listar_recebimentos(request):
	recebimentos = Recebimentos.objects.all()  # Busca todos os registros
	context = {'recebimentos': recebimentos}
	return render(request, 'pag_recebimentos.html', context)