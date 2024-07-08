from rest_framework import serializers
from .models import Terceros

class TercerosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Terceros
        fields = '__all__'
        read_only_fields = ('create_at', )


        """
        'id', 'nit', 'dv', 'razonSocial', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
                 'direccion', 'telefono', 'tipoDocumento', 'estadoRut', 'create_at', 'update_at'
        """