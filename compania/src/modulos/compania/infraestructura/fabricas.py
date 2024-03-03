""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from compania.src.seedwork.dominio.fabricas import Fabrica
from compania.src.seedwork.dominio.repositorios import Repositorio
from compania.src.modulos.compania.dominio.repositorios import RepositorioCompanias
from .repositorios import RepositorioCompaniasPostgress
# from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias.__class__:
            return RepositorioCompaniasPostgress()
        # elif obj == RepositorioProveedores.__class__:
        #     return RepositorioProveedoresSQLite()
        # else:
        #     raise ExcepcionFabrica()