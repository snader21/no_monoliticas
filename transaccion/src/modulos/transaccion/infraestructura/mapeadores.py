from transaccion.src.seedwork.dominio.repositorios import Mapeador
from transaccion.src.modulos.transaccion.dominio.objetos_valor import TipoTransaccion
from transaccion.src.modulos.transaccion.dominio.entidades import Transaccion
from .dto import Transaccion as TransaccionDTO


class MapeadorTransaccion(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        transaccion_dto = TransaccionDTO()

        transaccion_dto.descripcion = entidad.descripcion
        transaccion_dto.tipo = entidad.tipo
        transaccion_dto.compania_origen = entidad.compania_origen
        transaccion_dto.compania_destino = entidad.compania_destino
        transaccion_dto.pais_transaccion_origen = entidad.pais_transaccion_origen
        transaccion_dto.valor_transaccion_subtotal = entidad.valor_transaccion_subtotal
        transaccion_dto.impuesto_transaccion = entidad.impuesto_transaccion
        transaccion_dto.valor_transaccion_total = entidad.valor_transaccion_total
        transaccion_dto.id_propiedad = entidad.id_propiedad
        return transaccion_dto

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion._id = dto.id
        transaccion.descripcion = dto.descripcion
        transaccion.tipo = dto.tipo
        transaccion.compania_origen = dto.compania_origen
        transaccion.compania_destino = dto.compania_destino
        transaccion.pais_transaccion_origen = dto.pais_transaccion_origen
        transaccion.valor_transaccion_subtotal = dto.valor_transaccion_subtotal
        transaccion.impuesto_transaccion = dto.impuesto_transaccion
        transaccion.valor_transaccion_total = dto.valor_transaccion_total
        transaccion.id_propiedad = dto.id_propiedad
        return transaccion
