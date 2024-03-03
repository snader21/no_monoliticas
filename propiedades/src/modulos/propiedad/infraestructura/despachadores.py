import pulsar
from pulsar.schema import *

from src.modulos.propiedad.infraestructura.schema.v1.eventos import PropiedadCreadaPayload, EventoPropiedadCreada
from src.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        try:
            print('Publicando en el topico: ' + str(mensaje))
            cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            publicador = cliente.create_producer(
                topico, schema=AvroSchema(EventoPropiedadCreada))
            publicador.send(mensaje)
            cliente.close()
        except Exception as e:
            print('ERROR EN EL DESPACHADOR')
            print(e)

    def publicar_evento(self, evento, topico):
        payload = PropiedadCreadaPayload(
            id_propiedad=str(evento.id),
            direccion=str(evento.direccion)
        )
        evento_integracion = EventoPropiedadCreada(data=payload)
        self._publicar_mensaje(
            evento_integracion, topico, AvroSchema(PropiedadCreadaPayload))