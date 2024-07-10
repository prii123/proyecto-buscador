from ..models import Terceros
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TercerosSerializers
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TercerosViewSet(APIView):
    @swagger_auto_schema(
        operation_description="Busca datos en la base de datos y en DIAN.",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "nit": openapi.Schema(type=openapi.TYPE_INTEGER, description='NIT/CC'),
                    "dv": openapi.Schema(type=openapi.TYPE_INTEGER, description='DV'),
                    "razonSocial": openapi.Schema(type=openapi.TYPE_STRING, description='RAZON SOCIAL'),
                    "nombre1": openapi.Schema(type=openapi.TYPE_STRING, description='NOMBRE 1'),
                    "nombre2": openapi.Schema(type=openapi.TYPE_STRING, description='NOMBRE 2'),
                    "apellido1": openapi.Schema(type=openapi.TYPE_STRING, description='APELLIDO 1'),
                    "apellido2": openapi.Schema(type=openapi.TYPE_STRING, description='APELLIDO 2'),
                    "direccion": openapi.Schema(type=openapi.TYPE_STRING, description='DIRECCION'),
                    "telefono": openapi.Schema(type=openapi.TYPE_STRING, description='TELEFONO'),
                    "tipoDocumento": openapi.Schema(type=openapi.TYPE_STRING, description='TIPO DOCUMENTO'),
                    "estadoRut": openapi.Schema(type=openapi.TYPE_STRING, description='ESTADO RUT')
                },
            ),
        ),
        responses={
            200: openapi.Response(
                description="Respuesta del Servidor",
                examples={
                    "application/json": {
                        "message": "OK"
                    }
                }
            ),
        }
    )
    def post(self, request):
        try:
            serializer = TercerosSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'OK'}, status= status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)

    """ """
    @swagger_auto_schema(
    #method='get',
    responses={
        200: openapi.Response(
            description="Inicio de sesión exitoso",
            examples={
                "application/json": {
                    "id": "int",
                    "nit": "int",
                    "dv": "int",
                    "razonSocial": "string",
                    "nombre1": "string",
                    "nombre2": "string",
                    "apellido1": "string",
                    "apellido2": "string",
                    "direccion": "string",
                    "telefono": "string",
                    "tipoDocumento": "string",
                    "estadoRut": "string",
                    "create_at": "string",
                    "update_at": "string"
                }
            }
        ),
        #400: openapi.Response(description="Credenciales inválidas"),
    }
)
    
    def get(self, request):
        try:
            terceros = Terceros.objects.all()
            serializer = TercerosSerializers(terceros, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)


