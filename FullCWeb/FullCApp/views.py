# //----- IMPORTS -----// 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login

# //----- VISTAS -----// 

# //----- INICIO VISTA -----// 

def inicio(request):
    servicios = Servicio.objects.all()
    data = {
        'servicios' : servicios
    }
    return render(request, 'FullCApp/inicio.html', data)

# //----- CONTACTO VISTA -----// 

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST) # recibe los datos del form
        if formulario.is_valid(): #si el form es valido se guarda
            formulario.save()
            messages.success(request, 'Peticion Enviada correctamente!')
        else:
            data["form"] = formulario


    return render(request, 'FullCApp/contacto.html', data)

def sobre_nosotros(request):

    return render(request, 'FullCApp/sobre_nosotros.html')

# //----- INICIO VISTA -----// 

def servicios(request):
    servicios = Servicio.objects.all()
    data = {
        'servicios' : servicios
    }
    return render(request, 'Servicios/servicios.html', data)

