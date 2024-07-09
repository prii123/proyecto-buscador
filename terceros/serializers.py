from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Terceros

class TercerosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Terceros
        fields = '__all__'
        read_only_fields = ('create_at', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'