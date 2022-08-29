from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Noticia
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from core.mixins import AdminRequired
from .forms import CrearNoticiaForm


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

def editar_noticia(request):
    return render(request, 'secciones/editar.html')

class DetalleNoticia(DetailView):
    model = Noticia
    template_name = "secciones/detalle_noticia.html"