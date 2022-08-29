from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Archivo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from core.mixins import AdminRequired
from .forms import CargarArchivoForm
import mimetypes
import os

# Create your views here.


class ListaDescargas(ListView):
    template_name= "descargas.html"
    model = Archivo
    context_object_name= "archivos"
    def get_queryset(self):
        return Archivo.objects.all().order_by("created_date")

class CrearDescarga(AdminRequired, LoginRequiredMixin, CreateView):
    template_name= "crear.html"
    model = Archivo
    form_class = CargarArchivoForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author_id = self.request.user.id
        return super(CrearDescarga, self).form_valid(form) 

    def get_success_url(self, **kwargs):
        return reverse('descargas')

class BorrarArchivo(AdminRequired, LoginRequiredMixin, DeleteView):
    model = Archivo
    template_name = "borrar.html"

    def get_success_url(self, **kwargs):
        return reverse('descargas')