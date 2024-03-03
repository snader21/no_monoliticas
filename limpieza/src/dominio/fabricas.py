
from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Mapeador
from seedwork.dominio.entidades import Entidad
from seedwork.dominio.entidades import Tra
from src.dominio.entidades import Propiedad

@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)
            propiedad.crear_propiedad()
            return propiedad
