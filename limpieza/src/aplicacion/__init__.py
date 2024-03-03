from pydispatch import dispatcher

from .handler import HandlerCompaniaIntegracion
from src.dominio.eventos import PropiedadActualizada


dispatcher.connect(HandlerCompaniaIntegracion.handle_propiedad_actualizada, signal=f'{PropiedadActualizada.__name__}Dominio')