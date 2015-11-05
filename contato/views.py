from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'contato/index.html',{})

def login(request): 
	return render(request, 'contato/login.html', {})

def cadastro(request):
	return render(request, 'contato/cadastro.html', {})