# //---- IMPORTS ----//

from django.db import models

#//----- CLASES -----//

# //----- CLASE SERVICIO -----// 

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="servicios", null=True)

    def __str__(self):
        return self.nombre

# //----- CLASE PRESTACION -----// 

class Prestacion(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=100)
    a_materno = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.servicio

# //----- CLASE CONTACTO -----//

class Contacto(models.Model):
    opciones_consultas = [
        [0, "consulta"],
        [1, "reclamo"],
        [2, "sugerencia"],
        [3, "felicitaciones"]
    ]
    nombre = models.CharField(max_length=50)
    a_paterno = models.CharField(max_length=100)
    a_materno = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.IntegerField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return tipo_consulta