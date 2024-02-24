from src.recopilacion.seedwork.aplicacion.comandos import ComandoHandler
from src.recopilacion.modulos.compania.infraestructura.fabricas import FabricaRepositorio
from src.recopilacion.modulos.compania.dominio.fabricas import FabricaCompania

class CrearCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_compania: FabricaCompania = FabricaCompania()
        
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_compania(self):
        return self._fabrica_compania    
    