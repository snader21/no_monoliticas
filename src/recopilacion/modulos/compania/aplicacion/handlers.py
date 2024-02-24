from src.recopilacion.modulos.compania.dominio.eventos import PaisActualizado
from src.recopilacion.seedwork.aplicacion.handlers import Handler
from src.recopilacion.modulos.compania.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_pais_actualizado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')


    