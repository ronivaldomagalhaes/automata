from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello, world. You're at the cadastro index.")

def detail (request, cadastro_id):
	return HttpResponse("Voce esta visualizando o cadastro %s." % cadastro_id)

