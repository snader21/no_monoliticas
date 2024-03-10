from dataclasses import dataclass, field
from src.seedwork.dominio.fabricas import Fabrica
from src.seedwork.dominio.repositorios import Repositorio
from src.dominio.repositorios import RepositorioSaga
from .repositorios import RepositorioSagaPostgress


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioSaga.__class__:
            return RepositorioSagaPostgress()
        # elif obj == RepositorioProveedores.__class__:
        #     return RepositorioProveedoresSQLite()
        # else:
        #     raise ExcepcionFabrica()