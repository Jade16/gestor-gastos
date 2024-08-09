from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def usuario(request):
	if request.method == 'POST':
		print("Recebendo POST request")
		form = UsuarioForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			form.save()
			print("Formulário válido e salvo com sucesso!")
			return redirect('usuario')  # Redirecionar para a lista de recebimentos
		else:
			print("Formulário inválido: ", form.errors)
	else:
		form = UsuarioForm()
	
	context = {'form': form}
	return render(request, 'pag_usuario.html', context)

# def mostrar_foto(request):
# 	recebimentos = Recebimentos.objects.all()  # Busca todos os registros
# 	context = {'recebimentos': recebimentos}
# 	return render(request, 'pag_recebimentos.html', context)