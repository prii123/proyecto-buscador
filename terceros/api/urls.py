from rest_framework import routers
from .tercerosViewSet import TercerosViewSet
from .buscadorTerceros import SearchDataAPIView
from django.urls import path

"""
router = routers.DefaultRouter()
router.register('terceros', TercerosViewSet, 'terceros')
#router.register('api/v1/busca-tercero', SearchDataAPIView, 'buscaterceros')

urlpatterns = router.urls

"""
urlpatterns = [
    path('terceros/', TercerosViewSet.as_view(), name='terceros'),
    path('terceros2/', SearchDataAPIView.as_view(), name='terceros2'),
]


