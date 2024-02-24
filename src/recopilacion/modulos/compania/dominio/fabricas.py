""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Compania
from .reglas import PaisesValidos
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from src.recopilacion.seedwork.dominio.repositorios import Mapeador, Repositorio
from src.recopilacion.seedwork.dominio.fabricas import Fabrica
from src.recopilacion.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)

            self.validar_regla(PaisesValidos(compania.pais))
            # Agregar mas reglas de ser necesario

            return compania
