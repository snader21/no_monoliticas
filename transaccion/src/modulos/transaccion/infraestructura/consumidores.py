import pulsar,_pulsar  
from transaccion.src.app import app
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from transaccion.src.modulos.transaccion.aplicacion.servicios import ServicioTransaccion

from transaccion.src.modulos.transaccion.infraestructura.schema.v1.eventos import PaisActualizadoPayload
from transaccion.src.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(PaisActualizadoPayload))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido desde transacciones: {mensaje.value()}')
            with app.app_context():
                ServicioTransaccion().actualizar_impuestos(mensaje.value().id_compania, mensaje.value().pais_nuevo)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()