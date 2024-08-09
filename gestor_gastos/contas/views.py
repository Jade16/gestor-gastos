from django.shortcuts import render, redirect
from .models import Contas
from .forms import ContaForm
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def contas(request):
	if request.method == 'POST':
		print("Contas POST request")
		form = ContaForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			form.save()
			print("Formulário válido e salvo com sucesso!")
			return redirect('listar_contas')  # Redirecionar para a lista de contas
		else:
			print("Formulário inválido: ", form.errors)
	else:
		form = ContaForm()
	
	context = {'form': form}
	return render(request, 'pag_contas.html', context)

def listar_contas(request):
	contas = Contas.objects.all()  # Busca todos os registros
	context = {'contas': contas}
	return render(request, 'pag_contas.html', context)