import pulsar
import _pulsar
from transaccion.src.app import app
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from transaccion.src.modulos.transaccion.aplicacion.servicios import ServicioTransaccion

from transaccion.src.modulos.transaccion.infraestructura.schema.v1.eventos import PaisActualizadoPayload
from transaccion.src.seedwork.infraestructura import utils
from transaccion.src.modulos.transaccion.infraestructura.schema.v1.comandos import ComandoCrearTransaccionPayload, ComandoBorrarTransaccionPayload


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(PaisActualizadoPayload))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido desde transacciones: {mensaje.value()}')
            with app.app_context():
                ServicioTransaccion().actualizar_impuestos(
                    mensaje.value().id_compania, mensaje.value().pais_nuevo)
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comando_creacion():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('crear-transaccion', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='transaccion-sub-eventos', schema=AvroSchema(ComandoCrearTransaccionPayload))

        while True:
            mensaje = consumidor.receive()
            print(
                f'Evento de creacion de transacciones recibido: {mensaje.value()}')
            with app.app_context():
                ServicioTransaccion().crear_transaccion(
                    mensaje.value().descripcion,
                    mensaje.value().tipo,
                    mensaje.value().compania_origen,
                    mensaje.value().compania_destino,
                    mensaje.value().pais_transaccion_origen,
                    mensaje.value().valor_transaccion_subtotal,
                    mensaje.value().id_propiedad
                )
            consumidor.acknowledge(mensaje)
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de eventos crear transaccion!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comando_eliminacion():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('borrar-transaccion', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='transaccion-sub-eventos', schema=AvroSchema(ComandoBorrarTransaccionPayload))

        while True:
            mensaje = consumidor.receive()
            print(
                f'Evento de eliminacion de transacciones recibido: {mensaje.value()}')
            with app.app_context():
                ServicioTransaccion().borrar_transaccion(mensaje.value().id_transaccion)
            consumidor.acknowledge(mensaje)
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de eventos borrar transaccion!')
        traceback.print_exc()
        if cliente:
            cliente.close()
