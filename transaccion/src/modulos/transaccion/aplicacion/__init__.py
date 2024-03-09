from pydispatch import dispatcher

from .handlers import HandlerTransaccionIntegracion

from transaccion.src.modulos.transaccion.dominio.eventos import VentaRealizada

dispatcher.connect(HandlerTransaccionIntegracion.handle_venta_realizada,
                   signal=f'{VentaRealizada.__name__}Dominio')
dispatcher.connect(
    HandlerTransaccionIntegracion.handle_transaccion_creada, signal='TransaccionCreada')
dispatcher.connect(HandlerTransaccionIntegracion.handle_creacion_de_transaccion_fallida,
                   signal='ErrorCreandoTransaccion')
