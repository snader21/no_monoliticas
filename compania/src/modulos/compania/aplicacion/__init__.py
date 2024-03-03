from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion

from compania.src.modulos.compania.dominio.eventos import PaisActualizado

dispatcher.connect(HandlerCompaniaIntegracion.handle_pais_actualizado, signal=f'{PaisActualizado.__name__}Dominio')