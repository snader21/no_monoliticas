import pulsar
from pulsar.schema import *

from transaccion.src.modulos.transaccion.infraestructura.schema.v1.eventos import VentaRealizadaPayload
from transaccion.src.modulos.transaccion.infraestructura.schema.v1.comandos import ComandoCrearReserva, ComandoCrearReservaPayload
from transaccion.src.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        try:
            print('Publicando en el topico: ' + str(mensaje))
            cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            publicador = cliente.create_producer(topico, schema)
            publicador.send(mensaje)
            cliente.close()
        except Exception as e:
            print('ERROR EN EL DESPACHADOR')
            print(e)

    def publicar_evento(self, evento, topico):
        payload = VentaRealizadaPayload(
            id_propiedad=str(evento.id_propiedad),
            compania_destino_id=str(evento.compania_destino)
        )
        self._publicar_mensaje(
            payload, topico, AvroSchema(VentaRealizadaPayload))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearReservaPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearReserva(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoCrearReserva))
