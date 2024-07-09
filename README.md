# BUSCADOR DIAN Y OTROS


1. tener el servidor de redis 
2. activar celery con el siguiente comando
```código
celery -A buscador worker -l info -P eventlet
```

3. activar proyecto de DJANGO  
```código
python manage.py runserver
```
