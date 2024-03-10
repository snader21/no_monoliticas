import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from src.infraestructura.util import broker_host
from src.infraestructura.schema.v1.eventos import CompaniaCreadaPayload, CompaniaFallidaPayload, PropiedadCreadaPayload, PropiedadFallidaPayload, TransaccionCreadaPayload, TransaccionFallidaPayload
from src.aplicacion.coordinadores.saga_transacciones import ejecutarComandoCompania, ejecutarComandoTransaccion, ejecutarComandoCompensarCompania, ejecutarComandoCompensarPropiedad
from src.app import app

def suscribirse_a_compania_creada():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('compania-creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(CompaniaCreadaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido compania creada: {mensaje.value()}')
            with app.app_context():
                ejecutarComandoCompania(mensaje.value().id_compania, mensaje.value().id_correlacion, mensaje.value().tipo)
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de compania creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_compania_fallida():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('creacion-de-compania-fallida', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(CompaniaFallidaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido compania fallida: {mensaje.value()}')
            with app.app_context():
                # TODO
                ...
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de compania fallida!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_propiedad_creada():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('propiedad-creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(PropiedadCreadaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido propiedad creada: {mensaje.value()}')
            with app.app_context():
                ejecutarComandoTransaccion(mensaje.value().id_propiedad, mensaje.value().id_correlacion)
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de propiedad creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_propiedad_fallida():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('propiedad_fallida', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(PropiedadFallidaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido propiedad fallida: {mensaje.value()}')
            with app.app_context():
                ejecutarComandoCompensarCompania(mensaje.value().id_correlacion)
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de propiedad fallida!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_transaccion_creada():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('transaccion-creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(TransaccionCreadaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido transaccion creada: {mensaje.value()}')
            with app.app_context():
                # TODO
                ...
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de transaccion creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_transaccion_fallida():
    try:
        cliente = None
        cliente = pulsar.Client(f'pulsar://{broker_host()}:6650')
        consumidor = cliente.subscribe('transaccion_fallida', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saga-sub-eventos', schema=AvroSchema(TransaccionFallidaPayload))
    
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido transaccion fallida: {mensaje.value()}')
            with app.app_context():
                ejecutarComandoCompensarPropiedad(mensaje.value().id_correlacion)
                ejecutarComandoCompensarCompania(mensaje.value().id_correlacion)
            consumidor.acknowledge(mensaje)     
    except:
        logging.error('ERROR: Suscribiendose al tópico de transaccion fallida!')
        traceback.print_exc()
        if cliente:
            cliente.close()