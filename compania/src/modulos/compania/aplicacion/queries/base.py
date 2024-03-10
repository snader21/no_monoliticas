from src.seedwork.aplicacion.queries import QueryHandler
from src.modulos.compania.infraestructura.fabricas import FabricaRepositorio
from src.modulos.compania.dominio.fabricas import FabricaCompania

class CompaniaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_compania: FabricaCompania = FabricaCompania()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_compania    