
#import threading
from ..models import Terceros
from django.http import JsonResponse
from rest_framework.views import APIView
from .tasks import realizar_busquedas_dian
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class SearchDataAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Busca datos en la base de datos y en DIAN.",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'nit': openapi.Schema(type=openapi.TYPE_INTEGER, description='NIT/CC'),
                },
            ),
        ),
        responses={
            200: openapi.Response(
                description="Respuesta del Servidor",
                examples={
                    "application/json": {
                        "OK": [
                            {
                                "nit": 12345,
                                "nit": 12346,
                                "nit": 12347
                                # Otros campos relevantes de la respuesta
                            }
                        ],
                        "DIAN": [
                            {
                                "nit":123543,
                                "nit":123543
                            }
                            ],
                    }
                }
            ),
        }
    )

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



