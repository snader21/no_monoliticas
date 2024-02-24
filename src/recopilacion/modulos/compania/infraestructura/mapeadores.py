""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from src.recopilacion.seedwork.dominio.repositorios import Mapeador
from src.recopilacion.modulos.compania.dominio.objetos_valor import TipoCompania, TipoPersona
from src.recopilacion.modulos.compania.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO

class MapeadorCompania(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.id = str(entidad.id)
        compania_dto.nombre = str(entidad.nombre)
        compania_dto.identificacion = str(entidad.identificacion)
        compania_dto.pais = str(entidad.pais)
        compania_dto.tipo = entidad.tipo.value
        compania_dto.tipoPersona = entidad.tipoPersona.value
        return compania_dto
    
    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        compania._id = dto.id
        compania.nombre = dto.nombre
        compania.identificacion = dto.identificacion
        compania.pais = dto.pais
        compania.tipo = dto.tipo
        compania.tipoPersona = dto.tipoPersona
        
        return compania