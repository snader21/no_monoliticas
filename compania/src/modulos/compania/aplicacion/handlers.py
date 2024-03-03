from compania.src.modulos.compania.dominio.eventos import PaisActualizado
from compania.src.seedwork.aplicacion.handlers import Handler
from compania.src.modulos.compania.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_pais_actualizado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')


    