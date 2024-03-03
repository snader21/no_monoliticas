from src.seedwork.aplicacion.handlers import Handler
from src.infrastructura.despachadores import Despachador


class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_propiedad_actualizada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-limpieza')


    