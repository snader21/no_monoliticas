import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from src.recopilacion.modulos.transaccion.aplicacion.servicios import ServicioReserva

from src.recopilacion.modulos.transaccion.infraestructura.schema.v1.eventos import PaisActualizadoPayload
from src.recopilacion.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(PaisActualizadoPayload))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido desde transacciones: {mensaje.value()}')
            ServicioReserva().actualizar_impuestos(mensaje.value().id_compania, mensaje.value().pais_nuevo)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()