from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion

from src.modulos.propiedad.dominio.eventos import PropiedadCreada

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creada,
                   signal=f'{PropiedadCreada.__name__}Integracion')
