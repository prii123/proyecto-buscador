from celery import shared_task
from ..dian.buscadorDian import buscadorDIAN

@shared_task
def realizar_busquedas_dian(missing_ids):
    buscador = buscadorDIAN(missing_ids, 'xxxxxxxx')
    buscador.multiples_busquedas()
    data_return = buscador.retornar_datos()
    #print(data_return)
    return data_return
