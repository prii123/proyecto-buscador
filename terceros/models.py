from django.db import models

# Create your models here.
class Terceros(models.Model):
    nit = models.CharField(max_length=20)
    dv = models.CharField(max_length=1)
    razonSocial = models.CharField(max_length=200)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=10)
    estadoRut = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

