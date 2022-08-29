from django import forms
from .models import Comentario, Noticia

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class CrearNoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["title", "text", "picture"]
        labels = {
            'title' : 'Título',
            'text' : 'Noticia',
            'picture': 'Foto',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título de la noticia'}),
            'text' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe la noticia'})
        }

class CrearComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["comment"]
        labels = {
            'comment' : 'Comentar',
        }

        widgets = {
            'comment' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu comentario'})
        }