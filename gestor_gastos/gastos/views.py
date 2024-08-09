from django.shortcuts import render, redirect
from .models import Gastos
from .forms import GastoForm
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def gastos(request):
	if request.method == 'POST':
		print("Gastos POST request")
		form = GastoForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			form.save()
			print("Formulário válido e salvo com sucesso!")
			return redirect('listar_gastos')  # Redirecionar para a lista de recebimentos
		else:
			print("Formulário inválido: ", form.errors)
	else:
		form = GastoForm()
	
	context = {'form': form}
	return render(request, 'pag_gastos.html', context)

def listar_gastos(request):
	gastos = Gastos.objects.all()  # Busca todos os registros
	context = {'gastos': gastos}
	return render(request, 'pag_gastos.html', context)