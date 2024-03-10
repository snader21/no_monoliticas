from src.modulos.compania.dominio.eventos import PaisActualizado
from src.modulos.compania.infraestructura.schema.v1.eventos import CompaniaCreadaPayload, CreacionDeCompaniaFallidaPayload
from src.seedwork.aplicacion.handlers import Handler
from src.modulos.compania.infraestructura.despachadores import Despachador
from pulsar.schema import AvroSchema

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_pais_actualizado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')
    
    @staticmethod
    def handle_compania_creada(evento):
        print('HandlerCompaniaIntegracion.handle_compania_creada!!!!!!!')
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=CompaniaCreadaPayload(id_compania=evento.id, tipo_compania=evento.tipo_compania, id_correlacion=evento.id_correlacion), topico='compania-creada', schema=AvroSchema(CompaniaCreadaPayload))
    
    @staticmethod
    def handle_creacion_de_compania_fallida(id_correlacion):
        despachador = Despachador()
        despachador._publicar_mensaje(mensaje=CreacionDeCompaniaFallidaPayload(id_correlacion=id_correlacion), topico='creacion-de-compania-fallida', schema=AvroSchema(CreacionDeCompaniaFallidaPayload))


    