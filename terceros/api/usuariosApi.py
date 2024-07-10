from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
        },
        required=['username', 'password']
    ),
    responses={
        200: openapi.Response(
            description="Inicio de sesión exitoso",
            examples={
                "application/json": {
                    "token": "string",
                    "user": {
                       "id": "int",
                       "last_login": 'string',
                       "is_superuser": 'string',
                       "username": "string",
                       "first_name": "string",
                       "last_name": "string",
                       "email": "string",
                       "is_staff": 'boolean',
                       "is_active": 'boolean',
                       "date_joined": "date",
                    }
                }
            }
        ),
        400: openapi.Response(description="Credenciales inválidas"),
    }
)

@api_view(['POST'])
def login(request):
    user=get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error':'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({'token':token.key, 'user':serializer.data}, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo electronico'),
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
        },
        required=['email', 'username', 'password']
    ),
    responses={
        200: openapi.Response(
            description="Inicio de sesión exitoso",
            examples={
                "application/json": {
                    "token": "string",
                    "user": {
                       "id": "int",
                       "last_login": 'string',
                       "is_superuser": 'string',
                       "username": "string",
                       "first_name": "string",
                       "last_name": "string",
                       "email": "string",
                       "is_staff": 'boolean',
                       "is_active": 'boolean',
                       "date_joined": "date",
                    }
                }
            }
        ),
        400: openapi.Response(description="Datos invalidos"),
    }
)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description="Inicio de sesión exitoso",
            examples={
                "application/json": {
                    "message": "string",
                }
            }
        ),
        #400: openapi.Response(description="Credenciales inválidas"),
    }
)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({"message": "estas logueado con {}".format(request.user.username)}, status=status.HTTP_200_OK)