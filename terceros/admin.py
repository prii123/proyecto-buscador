from django.contrib import admin
from .models import Terceros


@admin.register(Terceros)
class TerceroAdmin(admin.ModelAdmin):
    list_display = ['nit', 'dv', 'razonSocial', 'nombre1', 'nombre2', 'apellido1', 'apellido2']


