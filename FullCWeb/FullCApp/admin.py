# //----- IMPORTS -----// 

from django.contrib import admin
from .models import *
from .forms import *

# //----- CLASES -----//

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre','a_paterno','correo','telefono']
    search_fields = ['nombre']
    list_filter = ['a_paterno','correo','telefono']
    list_per_page = 5

class PrestacionAdmin(admin.ModelAdmin):
    list_display = ['nombre','a_paterno','telefono','servicio']
    search_fields = ['nombre']
    list_filter = ['a_paterno','telefono','servicio']
    list_per_page = 5

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']
    search_fields = ['nombre']
    list_per_page = 5

# //----- REGISTROS EN ADMIN  -----// 

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Prestacion, PrestacionAdmin)
admin.site.register(Contacto, ContactoAdmin)
