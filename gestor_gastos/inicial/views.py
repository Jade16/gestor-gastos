from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicial(request):
	template = loader.get_template('pag_inicial.html')
	return HttpResponse(template.render())