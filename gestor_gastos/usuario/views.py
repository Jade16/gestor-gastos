from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def usuario(request):
	template = loader.get_template('pag_usuario.html')
	return HttpResponse(template.render())