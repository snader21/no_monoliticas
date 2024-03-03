from src.seedwork.dominio.repositorios import Mapeador
from src.modulos.propiedad.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO


class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()

        propiedad_dto.compania_duena = entidad.compania_duena
        propiedad_dto.compania_arrendataria = entidad.compania_arrendataria
        propiedad_dto.direccion = entidad.direccion
        propiedad_dto.pais_ubicacion = entidad.pais_ubicacion
        propiedad_dto.tamano = entidad.tamano
        propiedad_dto.latitud = entidad.latitud
        propiedad_dto.longitud = entidad.longitud
        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad._id = str(dto.id)
        propiedad.compania_duena = str(dto.compania_duena)
        propiedad.compania_arrendataria = str(dto.compania_arrendataria)
        propiedad.direccion = dto.direccion
        propiedad.pais_ubicacion = dto.pais_ubicacion
        propiedad.tamano = dto.tamano
        propiedad.latitud = dto.latitud
        propiedad.longitud = dto.longitud
        return propiedad
