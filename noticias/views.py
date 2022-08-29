from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Comentario, Noticia
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from core.mixins import AdminRequired
from .forms import CrearNoticiaForm, CrearComentarioForm


class ListaNoticias(ListView):
    template_name= "secciones/index.html"
    model = Noticia
    context_object_name= "noticias"
    def get_queryset(self):
        return Noticia.objects.all().order_by("created_date")


class CrearNoticias(AdminRequired, LoginRequiredMixin, CreateView):
    template_name= "secciones/crear.html"
    model = Noticia
    form_class = CrearNoticiaForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author_id = self.request.user.id
        return super(CrearNoticias, self).form_valid(form) 

    def get_success_url(self, **kwargs):
        return reverse('noticias')


class DetalleNoticia(DetailView):
    model = Noticia
    template_name = "secciones/detalle_noticia.html"

class EditarNoticia(AdminRequired, LoginRequiredMixin, UpdateView):
    model = Noticia
    template_name = "secciones/editar.html"
    form_class = CrearNoticiaForm

    def get_success_url(self, **kwargs):
        return reverse('noticias')

class BorrarNoticia(AdminRequired, LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = "secciones/borrar.html"

    def get_success_url(self, **kwargs):
        return reverse('noticias')

class CrearComentario(LoginRequiredMixin, CreateView):
    template_name= "secciones/comentar.html"
    model = Comentario
    form_class = CrearComentarioForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creator_id = self.request.user.id
        f.noticia_id = self.kwargs['pk']
        return super(CrearComentario, self).form_valid(form) 

    def get_success_url(self, **kwargs):
        return (f'../detalle/{self.kwargs["pk"]}')

class BorrarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = "secciones/borrar_comentario.html"

    def get_success_url(self, **kwargs):
        return (f'../')
        