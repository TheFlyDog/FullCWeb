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
    path('servicios/', servicios, name="servicios")
] 