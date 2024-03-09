from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion

from src.modulos.compania.dominio.eventos import PaisActualizado

dispatcher.connect(HandlerCompaniaIntegracion.handle_pais_actualizado, signal=f'{PaisActualizado.__name__}Dominio')
dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_creada, signal='CompaniaCreada')
dispatcher.connect(HandlerCompaniaIntegracion.handle_creacion_de_compania_fallida, signal='ErrorCreandoCompania')