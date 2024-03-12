from src.seedwork.aplicacion.dto import Mapeador as AppMap
from .dto import PropiedadDTO
from src.seedwork.dominio.repositorios import Mapeador as RepMap
from src.modulos.propiedad.dominio.entidades import Propiedad

from datetime import datetime


class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        compania_duena = externo.get("compania_duena")
        compania_arrendataria = externo.get("compania_arrendataria")
        direccion = externo.get("direccion")
        tamano = externo.get("tamano")
        pais_ubicacion = externo.get("pais_ubicacion")
        latitud = externo.get("latitud")
        longitud = externo.get("longitud")
        propiedad_dto = PropiedadDTO(
            compania_duena, compania_arrendataria, direccion, tamano, pais_ubicacion, latitud, longitud)
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        id_propiedad = str(entidad._id)
        compania_duena = entidad.compania_duena
        compania_arrendataria = entidad.compania_arrendataria
        direccion = entidad.direccion
        tamano = entidad.tamano
        pais_ubicacion = entidad.pais_ubicacion
        latitud = entidad.latitud
        longitud = entidad.longitud
        return PropiedadDTO(id_propiedad, compania_duena, compania_arrendataria, direccion, tamano, pais_ubicacion, latitud, longitud)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.compania_duena = dto.compania_duena
        propiedad.compania_arrendataria = dto.compania_arrendataria
        propiedad.direccion = dto.direccion
        propiedad.tamano = dto.tamano
        propiedad.pais_ubicacion = dto.pais_ubicacion
        propiedad.latitud = dto.latitud
        propiedad.longitud = dto.longitud

        return propiedad
