from pydispatch import dispatcher

from .handler import HandlerCompaniaIntegracion
from src.dominio.entidades import Propiedad


dispatcher.connect(HandlerCompaniaIntegracion.handle_propiedad_actualizada, signal=f'{Propiedad.__name__}Dominio')