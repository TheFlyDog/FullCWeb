# //----- IMPORTS -----// 

from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# //----- URLS -----// 

urlpatterns = [
    path('', inicio, name="inicio"),
    path('contacto/', contacto, name="contacto"),
    path('sobre-nosotros/', sobre_nosotros, name="sobre_nosotros"),
    path('servicios/', servicios, name="servicios"),
    path('agregar-prestacion/', agregar_prestacion, name="agregar_prestacion"),
    path('listar-prestacion/', listar_prestacion, name="listar_prestacion"),
    path('modificar-prestacion/<id>/', modificar_prestacion, name="modificar_prestacion"),
    path('eliminar-prestacion/<id>/', eliminar_prestacion, name="eliminar_prestacion"),
] 