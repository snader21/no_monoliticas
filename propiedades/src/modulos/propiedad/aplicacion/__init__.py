from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion

from src.modulos.propiedad.dominio.eventos import PropiedadCreada

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creada,
                   signal=f'{PropiedadCreada.__name__}Integracion')

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creada_saga, signal='PropiedadCreadaSaga')
dispatcher.connect(HandlerPropiedadIntegracion.handle_creacion_de_propiedad_fallida, signal='ErrorCreandoPropiedad')