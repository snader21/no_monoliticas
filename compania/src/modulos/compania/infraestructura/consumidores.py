import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from src.modulos.compania.aplicacion.servicios import ServicioCompania
from src.app import app
from src.modulos.compania.infraestructura.schema.v1.comandos import ComandoBorrarCompaniaPayload, ComandoCrearCompaniaPayload
from src.seedwork.infraestructura import utils

def suscribirse_a_comando_creacion():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('crear-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='compania-sub-eventos', schema=AvroSchema(ComandoCrearCompaniaPayload))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento de creacion de companias recibido: {mensaje.value()}')
            with app.app_context():
                ServicioCompania().crear_compania(
                    mensaje.value().tipoPersona, 
                    mensaje.value().nombre, 
                    mensaje.value().tipo, 
                    mensaje.value().pais, 
                    mensaje.value().identificacion,
                    mensaje.value().id_correlacion
                )
            consumidor.acknowledge(mensaje)
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos crear compania!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comando_eliminacion():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('borrar-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='compania-sub-eventos', schema=AvroSchema(ComandoBorrarCompaniaPayload))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento de eliminacion de companias recibido: {mensaje.value()}')
            with app.app_context():
                ServicioCompania().borrar_compania(
                    mensaje.value().id_compania
                )
            consumidor.acknowledge(mensaje)
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos borrar compania!')
        traceback.print_exc()
        if cliente:
            cliente.close()
        