from rest_framework import routers
from .tercerosViewSet import TercerosViewSet
from .buscadorTerceros import SearchDataAPIView
from django.urls import path, re_path
from ..api import usuariosApi


urlpatterns = [
    path('api/v1/terceros/', TercerosViewSet.as_view(), name='terceros'),
    path('api/v1/terceros-cliente/', SearchDataAPIView.as_view(), name='terceros-cliente'),
    re_path('api/v1/login', usuariosApi.login),
    re_path('api/v1/register', usuariosApi.register),
    re_path('api/v1/profile', usuariosApi.profile)
]




