from src.seedwork.aplicacion.queries import QueryHandler
from src.modulos.transaccion.infraestructura.fabricas import FabricaRepositorio
from src.modulos.transaccion.dominio.fabricas import FabricaTransaccion

class TransaccionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transaccion: FabricaTransaccion = FabricaTransaccion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_transaccion(self):
        return self._fabrica_transaccion    