import pulsar
import _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from src.app import app
from src.modulos.propiedad.aplicacion.servicios import ServicioPropiedad
from src.modulos.propiedad.infraestructura.schema.v1.eventos import (
    VentaRealizadaPayload,
    UbicacionActualizadaPayload
)
from src.seedwork.infraestructura import utils


def suscribirse_a_eventos_de_transacciones():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        # Consumidor para VentaRealizadaPayload
        consumidor_venta = cliente.subscribe(
            'eventos-transaccion',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='sub-eventos-venta',
            schema=AvroSchema(VentaRealizadaPayload)
        )

        while True:
            # Recepción de eventos de VentaRealizadaPayload
            mensaje_venta = consumidor_venta.receive()
            print(f'Evento de venta recibido: {mensaje_venta.value()}')
            with app.app_context():
                ServicioPropiedad().actualizar_compania_duena(
                    mensaje_venta.value().id_propiedad,
                    mensaje_venta.value().compania_destino_id)
            consumidor_venta.acknowledge(mensaje_venta)

    except Exception as e:
        logging.error('ERROR: Suscribiendose a los tópicos de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_eventos_de_limpieza():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        # Consumidor para UbicacionActualizadaPayload
        consumidor_datos_geo = cliente.subscribe(
            'eventos-limpieza',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='sub-eventos-datos-limpieza',
            schema=AvroSchema(UbicacionActualizadaPayload)
        )

        while True:
            # Recepción de eventos de UbicacionActualizadaPayload
            mensaje_datos_geo = consumidor_datos_geo.receive()
            print(
                f'Evento de datos geográficos actualizados recibido: {mensaje_datos_geo.value()}')
            with app.app_context():
                ServicioPropiedad().actualizar_datos_geograficos(
                    mensaje_datos_geo.value().id_propiedad,
                    mensaje_datos_geo.value().latitud,
                    mensaje_datos_geo.value().longitud)
            consumidor_datos_geo.acknowledge(mensaje_datos_geo)

    except Exception as e:
        logging.error('ERROR: Suscribiendose a los tópicos de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
