""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from transaccion.src.seedwork.dominio.fabricas import Fabrica
from transaccion.src.seedwork.dominio.repositorios import Repositorio
from transaccion.src.modulos.transaccion.dominio.repositorios import RepositorioTransacciones
from .repositorios import RepositorioTransaccionesPostgress
# from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioTransacciones.__class__:
            return RepositorioTransaccionesPostgress()
        # elif obj == RepositorioProveedores.__class__:
        #     return RepositorioProveedoresSQLite()
        # else:
        #     raise ExcepcionFabrica()