from src.seedwork.aplicacion.handlers import Handler
from src.modulos.transaccion.infraestructura.despachadores import Despachador
from pulsar.schema import AvroSchema
from src.modulos.transaccion.infraestructura.schema.v1.eventos import CreacionDeTransaccionFallidaPayload, TransaccionCreadaPayload


class HandlerTransaccionIntegracion(Handler):

    @staticmethod
    def handle_venta_realizada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-transaccion')

    @staticmethod
    def handle_transaccion_creada(id_transaccion):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=TransaccionCreadaPayload(
            id_transaccion=id_transaccion), topico='transaccion-creada', schema=AvroSchema(TransaccionCreadaPayload))

    @staticmethod
    def handle_creacion_de_transaccion_fallida(id_correlacion):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=CreacionDeTransaccionFallidaPayload(
            id_correlacion=id_correlacion), topico='creacion-de-transaccion-fallida', schema=AvroSchema(CreacionDeTransaccionFallidaPayload))
