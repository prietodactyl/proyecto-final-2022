from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def quienes_somos(request):
    return render(request, 'paginas/quienes_somos.html')

def noticias(request):
    return render(request, 'noticias/index.html')

def crear_noticia(request):
    return render(request, 'noticias/crear.html')

def editar_noticia(request):
    return render(request, 'noticias/editar.html')

def descargas(request):
    return render(request, 'paginas/descargas.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')