import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from src.infraestructura.util import broker_host
from src.infraestructura.schema.v1.eventos import CompaniaCreadaPayload
from src.aplicacion.servicios import ServicioPropiead
from src.aplicacion.coordinadores.saga_transacciones import oir_mensaje
from src.aplicacion.eventos.compania_creada import CompaniaCreada
from src.app import app

def suscribirse_a_compania_creada():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('compania_creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(CompaniaCreadaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido compania creada: {mensaje.value()}')
            with app.app_context():
                local_storage.getItem()

                ServicioPropiead().maching_learning(mensaje.value().id_propiedad, mensaje.value().direccion)
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de compania creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()