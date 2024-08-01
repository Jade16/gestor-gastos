from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def gastos(request):
	if request.method == 'POST':
		print("Recebendo POST request")
		form = RecebimentoForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			form.save()
			print("Formulário válido e salvo com sucesso!")
			return redirect('listar_gastos')  # Redirecionar para a lista de recebimentos
		else:
			print("Formulário inválido: ", form.errors)
	else:
		form = RecebimentoForm()
	
	context = {'form': form}
	return render(request, 'pag_gastos.html', context)

def listar_gastos(request):
	gastos = Gastos.objects.all()  # Busca todos os registros
	context = {'gastos': gastos}
	return render(request, 'pag_gastos.html', context)