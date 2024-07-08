from rest_framework import routers
from .api import TercerosViewSet

router = routers.DefaultRouter()

router.register('api/terceros', TercerosViewSet, 'terceros')

urlpatterns = router.urls