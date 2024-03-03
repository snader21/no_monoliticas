from compania.src.seedwork.aplicacion.dto import Mapeador as AppMap
from .dto import CompaniaDTO
from compania.src.seedwork.dominio.repositorios import Mapeador as RepMap
from compania.src.modulos.compania.dominio.entidades import Compania
from compania.src.modulos.compania.dominio.objetos_valor import TipoCompania, TipoPersona

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):    
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        reserva_dto = CompaniaDTO()
        return reserva_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__

class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        nombres = entidad.nombre
        tipoPersona = entidad.tipoPersona.value
        tipo = entidad.tipo.value
        pais = entidad.pais
        identificacion = str(entidad.identificacion)
        return CompaniaDTO(nombres, tipoPersona, tipo, pais, identificacion)

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        compania.nombre = dto.nombre
        compania.identificacion = dto.identificacion
        compania.pais = dto.pais
        compania.tipo = TipoCompania(dto.tipo)
        compania.tipoPersona = TipoPersona(dto.tipoPersona)
        
        return compania


