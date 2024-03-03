import pulsar
from pulsar.schema import *

from src.infrastructura.util import broker_host
from src.dominio.eventos import PropiedadActualizada


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        try: 
            print('Publicando en el topico ya con el maching learnig ' + str(mensaje))
            cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
            publicador = cliente.create_producer(topico, schema=AvroSchema(PropiedadActualizada))
            publicador.send(mensaje)
            cliente.close()
        except Exception as e:
            print('ERROR EN EL DESPACHADOR')
            print(e)


    def publicar_evento(self, evento, topico):
        print(f'Evento: {evento}')
        payload = PropiedadActualizada(
            id_compania=str(evento.id), 
            ubicacion=evento.ubicacion,
            estrato=str(evento.etrato)
        )
        self._publicar_mensaje(payload, topico, AvroSchema(PropiedadActualizada))

