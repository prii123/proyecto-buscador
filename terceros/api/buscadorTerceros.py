
#import threading
from ..models import Terceros
from django.http import JsonResponse
from rest_framework.views import APIView

from ..dian.buscadorDian import buscadorDIAN

from .tasks import realizar_busquedas_dian



class SearchDataAPIView(APIView):

    def post(self, request):
        # Analiza los datos JSON del cuerpo de la solicitud
        data = request.data
        #print(data)

        # Extrae las identificaciones de los datos JSON
        nits = []
        for item in data:
            nits.append(item.get('nit'))
        #nits = data.get('nit', [])
        #print(nits)

        # Busca las identificaciones en la primera base de datos
        found_data1 = []

        missing_ids = []
        for nit in nits:
            try:
                model_instance = Terceros.objects.get(nit=nit)
                found_data1.append({
                    'nit': model_instance.id,
                    # Agrega otros datos relevantes de model_instance
                })
            except Terceros.DoesNotExist:
                missing_ids.append(nit)


        """
        buscador = buscadorDIAN(missing_ids, 'xxxxxxxx')
        buscador.multiples_busquedas()
        data_return = buscador.retornar_datos()
        print(data_return)
        """
        # Iniciar la búsqueda en DIAN en segundo plano con Celery
        task = realizar_busquedas_dian.delay(missing_ids)

        # Combina y retorna todos los datos
        combined_data = {
            'encontrado': found_data1,
            'Busqueda en dian': missing_ids,
            'hilo: ': str(task)

        }

        return JsonResponse(combined_data)


"""
        # Iniciar la búsqueda en DIAN en un hilo separado
        thread = threading.Thread(target=realizar_busquedas_dian, args=(missing_ids,))
        thread.start()
def realizar_busquedas_dian(missing_ids):
    buscador = buscadorDIAN(missing_ids, 'xxxxxxxx')
    buscador.multiples_busquedas()
    data_return = buscador.retornar_datos()
    print(data_return)

"""

