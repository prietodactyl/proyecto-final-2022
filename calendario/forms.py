from django import forms
from django.forms import ModelForm
from .models import Event



# crear un form de evento

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'description')
        labels = {
            'name': '', #aca se puede modificar lo que dice el formulario
            'event_date': '',
            'description':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Fecha del Evento'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descripción'})
        }

        