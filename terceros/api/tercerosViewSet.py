from ..models import Terceros
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TercerosSerializers
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TercerosViewSet(APIView):
    def post(self, request):
        try:
            serializer = TercerosSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'creado'}, status= status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        try:
            terceros = Terceros.objects.all()
            serializer = TercerosSerializers(terceros, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)


