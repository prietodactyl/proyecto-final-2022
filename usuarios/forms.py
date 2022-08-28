from pyexpat import model
from django import forms 

from django.contrib.auth.forms import UserCreationForm

from .models import Usuario
'''
class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=["first_name", "last_name", "username", "password1", "password2"]
        '''

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=["first_name", "last_name", "username", "password1", "password2"]
        labels = {
            'first_name': '', #aca se puede modificar lo que dice el formulario
            'last_name': '',
            'username':'',
            'password1':'',
            'password2':'',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Usuario'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Repetir contraseña'}),
        }