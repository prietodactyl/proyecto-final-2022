from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def noticias(request):
    return render(request, 'secciones/index.html')

@login_required
def crear_noticia(request):
    return render(request, 'secciones/crear.html')

def editar_noticia(request):
    return render(request, 'secciones/editar.html')