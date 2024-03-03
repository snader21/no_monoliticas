""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de transaccion

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de transaccion

"""

from transaccion.src import db
from transaccion.src.modulos.transaccion.dominio.repositorios import RepositorioTransacciones
from transaccion.src.modulos.transaccion.dominio.entidades import Transaccion
from transaccion.src.modulos.transaccion.dominio.fabricas import FabricaTransaccion
from transaccion.src.modulos.transaccion.infraestructura.mapeadores import MapeadorTransaccion
from .dto import Transaccion as TransaccionDTO
from .mapeadores import Mapeador
from uuid import UUID


class RepositorioTransaccionesPostgress(RepositorioTransacciones):
    def __init__(self):
        self._fabrica_transaccion: FabricaTransaccion = FabricaTransaccion()

    @property
    def fabrica_transaccion(self):
        return self._fabrica_transaccion

    def obtener_por_id(self, id: UUID) -> Transaccion:
        reserva_dto = db.session.query(
            TransaccionDTO).filter_by(id=str(id)).one()
        return self.fabrica_transaccion.crear_objeto(reserva_dto, MapeadorTransaccion())

    def obtener_por_compania_origen_id(self, id: UUID) -> list[Transaccion]:
        transacciones = db.session.query(
            TransaccionDTO).filter_by(compania_origen=str(id)).all()
        return [self.fabrica_transaccion.crear_objeto(transaccion_dto, MapeadorTransaccion()) for transaccion_dto in transacciones]

    def agregar(self, transaccion: Transaccion):
        transaccion_dto = self.fabrica_transaccion.crear_objeto(
            transaccion, MapeadorTransaccion())
        db.session.add(transaccion_dto)
        db.session.commit()

    def actualizar(self, transaccion: Transaccion):
        transaccion_dto = db.session.query(TransaccionDTO).filter_by(
            id=str(transaccion._id)).one()
        transaccion_dto.descripcion = transaccion.descripcion
        transaccion_dto.compania_origen = transaccion.compania_origen
        transaccion_dto.compania_destino = transaccion.compania_destino
        transaccion_dto.pais_transaccion_origen = transaccion.pais_transaccion_origen
        transaccion_dto.valor_transaccion_subtotal = transaccion.valor_transaccion_subtotal
        transaccion_dto.impuesto_transaccion = transaccion.impuesto_transaccion
        transaccion_dto.valor_transaccion_total = transaccion.valor_transaccion_total
        db.session.commit()
