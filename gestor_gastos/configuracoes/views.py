from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def configuracoes(request):
	template = loader.get_template('pag_configuracoes.html')
	return HttpResponse(template.render())