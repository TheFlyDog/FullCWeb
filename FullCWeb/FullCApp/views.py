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

# //----- AGREGAR PEDIDO VISTA -----// 

def agregar_prestacion(request):
    data = {
        'form' : PrestacionForm
    }


    if request.method == 'POST':
        formulario = PrestacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'La prestacion solicitada fue registrado exitosamente!')
        else:
            data["form"] = formulario

    return render(request, 'Prestaciones/agregar.html', data)

# //----- LISTAR PEDIDO VISTA -----// 


def listar_prestacion(request):
    prestaciones = Prestacion.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(prestaciones, 5) 
        prestaciones = paginator.page(page) 
    except:
        raise Http404

    data = {
        'entity' : prestaciones,
        'paginator': paginator
    }

    return render(request, 'Prestaciones/listar.html', data)

# //----- MODIFICAR PEDIDO VISTA -----// 

def modificar_prestacion(request, id):
    
    #busca el id obtenido en la url
    prestacion = get_object_or_404(Prestacion, id=id)

    data = {
        'form' : PrestacionForm(instance=prestacion)
    }

    if request.method == 'POST':
        formulario = PrestacionForm(data=request.POST, instance=prestacion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Los datos de la prestacion que solicito, se modificaron correctamente!")
            return redirect(to="listar_prestacion")
        else:
            data["form"] = formulario

    return render(request, 'Prestaciones/modificar.html', data)

# //----- ELIMINAR PEDIDO VISTA -----// 


def eliminar_prestacion(request, id):
    prestacion = get_object_or_404(PrestacionForm, id=id)
    prestacion.delete()
    messages.success(request, "La prestacion que había solicitado, se ha eliminado correctamente!")
    return redirect(to='listar_prestacion')