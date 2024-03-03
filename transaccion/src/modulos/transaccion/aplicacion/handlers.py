from transaccion.src.seedwork.aplicacion.handlers import Handler
from transaccion.src.modulos.transaccion.infraestructura.despachadores import Despachador

class HandlerTransaccionIntegracion(Handler):

    @staticmethod
    def handle_venta_realizada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-transaccion')


    