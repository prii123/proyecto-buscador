# BUSCADOR DIAN Y OTROS


1. tener el servidor de redis
2. activar celery con el siguiente comando
```código
celery -A buscador worker -l info -P eventlet
```
3. activar Flower - para monitorizar las tareas en ejecucion
http://localhost:5555/broker
```código
celery -A buscador flower
```

4. activar proyecto de DJANGO
```código
python manage.py runserver
```


pip install -r requirements.txt