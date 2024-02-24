from src.recopilacion.seedwork.aplicacion.dto import Mapeador as AppMap
from .dto import TransaccionDTO
from src.recopilacion.seedwork.dominio.repositorios import Mapeador as RepMap
from src.recopilacion.modulos.transaccion.dominio.entidades import Transaccion
from src.recopilacion.modulos.transaccion.dominio.objetos_valor import TipoTransaccion

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):    
    def externo_a_dto(self, externo: dict) -> TransaccionDTO:
        reserva_dto = TransaccionDTO()
        return reserva_dto

    def dto_a_externo(self, dto: TransaccionDTO) -> dict:
        return dto.__dict__

class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        descripcion = entidad.descripcion
        tipo = entidad.tipo
        compania_origen = entidad.compania_origen
        compania_destino = entidad.compania_destino
        pais_transaccion_origen = entidad.pais_transaccion_origen
        valor_transaccion_subtotal = entidad.valor_transaccion_subtotal
        return TransaccionDTO(descripcion,tipo,compania_origen, compania_destino,pais_transaccion_origen,valor_transaccion_subtotal)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.descripcion = dto.descripcion
        transaccion.tipo = TipoTransaccion(dto.tipo)
        transaccion.compania_origen = dto.compania_origen
        transaccion.compania_destino = dto.compania_destino
        transaccion.pais_transaccion_origen = dto.pais_transaccion_origen
        transaccion.valor_transaccion_subtotal = dto.valor_transaccion_subtotal
        return transaccion
