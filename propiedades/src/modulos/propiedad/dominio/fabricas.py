""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Propiedad
from .reglas import PaisesValidos, TamanoPositivo, EsRequerido
from src.seedwork.dominio.repositorios import Mapeador
from src.seedwork.dominio.fabricas import Fabrica
from src.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)

            self.validar_regla(EsRequerido(
                propiedad.compania_duena, 'La compania duena es requerida'))
            self.validar_regla(EsRequerido(
                propiedad.compania_arrendataria, 'La compania arrendataria es requerida'))
            self.validar_regla(EsRequerido(
                propiedad.direccion, 'La direccion es requerida'))
            self.validar_regla(EsRequerido(
                propiedad.pais_ubicacion, 'El pais es requerido'))
            self.validar_regla(EsRequerido(
                propiedad.tamano, 'El tamano es requerido'))
            self.validar_regla(TamanoPositivo(
                propiedad.tamano))
            self.validar_regla(PaisesValidos(
                propiedad.pais_ubicacion))

            return propiedad
