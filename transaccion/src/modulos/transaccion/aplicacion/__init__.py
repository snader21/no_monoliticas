from pydispatch import dispatcher

from .handlers import HandlerTransaccionIntegracion

from transaccion.src.modulos.transaccion.dominio.eventos import VentaRealizada

dispatcher.connect(HandlerTransaccionIntegracion.handle_venta_realizada, signal=f'{VentaRealizada.__name__}Dominio')