from src.modulos.propiedad.dominio.eventos import PropiedadCreada
from src.seedwork.aplicacion.handlers import Handler
from src.modulos.propiedad.infraestructura.despachadores import Despachador


class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')
