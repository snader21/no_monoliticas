from src.seedwork.aplicacion.dto import Mapeador as AppMap
from .dto import TransaccionDTO
from src.seedwork.dominio.repositorios import Mapeador as RepMap
from src.modulos.transaccion.dominio.entidades import Transaccion
from src.modulos.transaccion.dominio.objetos_valor import TipoTransaccion

from datetime import datetime


class MapeadorTransaccionDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> TransaccionDTO:
        descripcion = externo.get("descripcion")
        tipo = externo.get("tipo")
        compania_origen = externo.get("compania_origen")
        compania_destino = externo.get("compania_destino")
        pais_transaccion_origen = externo.get("pais_transaccion_origen")
        valor_transaccion_subtotal = externo.get("valor_transaccion_subtotal")
        id_propiedad = externo.get("id_propiedad")
        transaccion_dto = TransaccionDTO(
            descripcion, tipo, compania_origen, compania_destino, pais_transaccion_origen, valor_transaccion_subtotal, id_propiedad)
        return transaccion_dto

    def dto_a_externo(self, dto: TransaccionDTO) -> dict:
        return dto.__dict__


class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        descripcion = entidad.descripcion
        tipo = entidad.tipo.value
        compania_origen = str(entidad.compania_origen)
        compania_destino = str(entidad.compania_destino)
        pais_transaccion_origen = entidad.pais_transaccion_origen
        valor_transaccion_subtotal = entidad.valor_transaccion_subtotal
        id_propiedad = str(entidad.id_propiedad)
        return TransaccionDTO(descripcion, tipo, compania_origen, compania_destino, pais_transaccion_origen, valor_transaccion_subtotal, id_propiedad)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.descripcion = dto.descripcion
        transaccion.tipo = dto.tipo
        transaccion.compania_origen = dto.compania_origen
        transaccion.compania_destino = dto.compania_destino
        transaccion.pais_transaccion_origen = dto.pais_transaccion_origen
        transaccion.valor_transaccion_subtotal = dto.valor_transaccion_subtotal
        transaccion.id_propiedad = dto.id_propiedad
        return transaccion
