from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def primeira_view(request):
	return HttpResponse('hola mundo')

def template1(request):	
	name="RB"
	cores = [
        "mimosa",
        "verde",
        "vermelho",
    ]
	return render(request=request, template_name='index.html', context={'name':name, 'cores':cores})