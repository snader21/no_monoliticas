from src.seedwork.aplicacion.queries import QueryHandler
from src.modulos.propiedad.infraestructura.fabricas import FabricaRepositorio
from src.modulos.propiedad.dominio.fabricas import FabricaPropiedad


class PropiedadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad
