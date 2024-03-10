from src.seedwork.aplicacion.handlers import Handler
from src.infraestructura.despachadores import Despachador
from pulsar.schema import AvroSchema
from src.infraestructura.schema.v1.comandos import ComandoCompensarCompaniaPayload, ComandoCompensarPropiedadPayload, ComandoCrearCompaniaPayload, ComandoCrearPropiedadPayload, ComandoCrearTransaccionPayload


class HandlerTransaccionIntegracion(Handler):
    @staticmethod
    def handle_crear_compania(evento):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=evento, topico='crear-compania', schema=AvroSchema(ComandoCrearCompaniaPayload))

    @staticmethod
    def handle_crear_propiedad(evento):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=evento, topico='crear-propiedad', schema=AvroSchema(ComandoCrearPropiedadPayload))
    
    @staticmethod
    def handle_crear_transaccion(evento):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=evento, topico='crear-transaccion', schema=AvroSchema(ComandoCrearTransaccionPayload))
    
    @staticmethod
    def handle_compensar_compania(evento):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=evento, topico='borrar-compania', schema=AvroSchema(ComandoCompensarCompaniaPayload))
    
    @staticmethod
    def handle_compensar_propiedad(evento):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=evento, topico='borrar-propiedad', schema=AvroSchema(ComandoCompensarPropiedadPayload))

