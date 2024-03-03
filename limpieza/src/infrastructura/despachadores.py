import pulsar
from pulsar.schema import *

from src.infrastructura.util import broker_host
from src.infrastructura.schema.V1.eventos import PropiedadActualizadaPayload


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        try: 
            print('Publicando en el topico ya con el maching learnig ' + str(mensaje))
            cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
            publicador = cliente.create_producer(topico, schema=AvroSchema(PropiedadActualizadaPayload))
            publicador.send(mensaje)
            cliente.close()
        except Exception as e:
            print('ERROR EN EL DESPACHADOR')
            print(e)


    def publicar_evento(self, evento, topico):
        payload = PropiedadActualizadaPayload(
            id_compania=str(evento.id), 
            pais_nuevo=str(evento.pais)
        )
        self._publicar_mensaje(payload, topico, AvroSchema(PropiedadActualizadaPayload))

