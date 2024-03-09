from pulsar.schema import AvroSchema
from propiedades.src.modulos.propiedad.infraestructura.schema.v1.eventos import CreacionDePropiedadFallidaPayload
from src.modulos.propiedad.dominio.eventos import PropiedadCreada
from src.seedwork.aplicacion.handlers import Handler
from src.modulos.propiedad.infraestructura.despachadores import Despachador


class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')

    @staticmethod
    def handle_creacion_de_propiedad_fallida(id_correlacion):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=CreacionDePropiedadFallidaPayload(id_correlacion=id_correlacion), topico='creacion-de-propiedad-fallida', schema=AvroSchema(CreacionDePropiedadFallidaPayload))
