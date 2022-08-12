from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def noticias(request):
    return render(request, 'secciones/index.html')

def crear_noticia(request):
    return render(request, 'secciones/crear.html')

def editar_noticia(request):
    return render(request, 'secciones/editar.html')