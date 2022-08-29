from django import forms
from .models import Archivo

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class CargarArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ["title", "description", "archive"]
        labels = {
            'title' : 'Nombre',
            'description' : 'Descripción',
            'archive': 'Archivo',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del archivo'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripción del archivo'})
        }