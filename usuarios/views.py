from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render
from .forms import UsuarioRegistroForm
from .models import Usuario

'''
def registro(request):
    return render(request, 'registro.html')
    '''

class Registro(CreateView):
    model = Usuario
    form_class = UsuarioRegistroForm
    template_name = "registro.html"

    def get_success_url(self, **kwargs):
        return reverse('main')

