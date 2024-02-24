from src.recopilacion.seedwork.aplicacion.comandos import ComandoHandler
from src.recopilacion.modulos.transaccion.infraestructura.fabricas import FabricaRepositorio
from src.recopilacion.modulos.transaccion.dominio.fabricas import FabricaTransaccion

class CrearTransaccionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transaccion: FabricaTransaccion = FabricaTransaccion()
        
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_transaccion(self):
        return self._fabrica_transaccion