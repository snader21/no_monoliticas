from dataclasses import dataclass, field
from src.seedwork.dominio.fabricas import Fabrica
from src.seedwork.dominio.repositorios import Repositorio
from src.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioPropiedadesPostgress


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesPostgress()
        # elif obj == RepositorioProveedores.__class__:
        #     return RepositorioProveedoresSQLite()
        # else:
        #     raise ExcepcionFabrica()
