# //----- IMPORTS -----// 

from django import forms
from django.forms import ModelForm
from .models import *

# //----- FORMULARIOS -----// 

# //----- FORMULARIO CONTACTO -----// 

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ['nombre','a_paterno', 'a_materno', 'correo', 'telefono', 'tipo_consulta', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }
            ),

            'a_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }
            ),

            'a_materno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }
            ),

            'correo': forms.EmailInput(
                attrs={
                    'placeholder': 'correo@gmail.com',
                    'pattern': '[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}',
                    'class': 'form-control',
                    'required': 'true'
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'placeholder': '(9)12345678',
                    'max_length': '9',
                    'class': 'form-control',
                    'required': 'true'
                }
            ),
        }

# //----- FORMULARIO PRESTACION -----//

class PrestacionForm(forms.ModelForm):

    class Meta:
        model = Prestacion
        fields = '__all__' 