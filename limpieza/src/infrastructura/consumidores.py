import app
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from infrastructura.util import broker_host
from infrastructura.schema.V1.eventos import PropiedadActualizadaPayload
from src.aplicacion.servicios import ServicioPropiead



def suscribirse_a_eventos():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('evento-limpieza', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(PropiedadActualizadaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido desde algun lado, no se cual: {mensaje.value()}')
            with app.app_context():
                ServicioPropiead().maching_learning(mensaje.value())
            consumidor.acknowledge(mensaje)     
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()