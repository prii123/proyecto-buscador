from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el módulo de configuración de Django para el entorno 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buscador.settings')

app = Celery('buscador')

# Usar una cadena para configuración del módulo
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir tareas asíncronas en todas las aplicaciones instaladas de Django
app.autodiscover_tasks()
