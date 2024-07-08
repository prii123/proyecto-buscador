from .models import Terceros
from rest_framework import viewsets, permissions
from .serializers import TercerosSerializers

class TercerosViewSet(viewsets.ModelViewSet):
    queryset = Terceros.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TercerosSerializers
