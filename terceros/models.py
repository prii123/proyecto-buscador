from django.db import models

# Create your models here.
class Terceros(models.Model):
    nit = models.CharField(max_length=20)
    dv = models.CharField(max_length=1, blank=True, null=True)
    razonSocial = models.CharField(max_length=200, blank=True, null=True)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    apellido1 = models.CharField(max_length=50, blank=True, null=True)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    tipoDocumento = models.CharField(max_length=10, blank=True, null=True)
    estadoRut = models.CharField(max_length=10, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

