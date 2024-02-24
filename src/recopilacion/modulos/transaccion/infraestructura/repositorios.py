""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de transaccion

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de transaccion

"""

from src.recopilacion import db
from src.recopilacion.modulos.transaccion.dominio.repositorios import RepositorioTransacciones
from src.recopilacion.modulos.transaccion.dominio.entidades import Transaccion
from src.recopilacion.modulos.transaccion.dominio.fabricas import FabricaTransaccion
from src.recopilacion.modulos.transaccion.infraestructura.mapeadores import MapeadorTransaccion
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

    def obtener_por_compania_origen_id(self, id: UUID) -> Transaccion:
        reserva_dto = db.session.query(
            TransaccionDTO).filter_by(compania_origen=str(id)).one()
        return self.fabrica_transaccion.crear_objeto(reserva_dto, MapeadorTransaccion())

    def agregar(self, transaccion: Transaccion):
        transaccion_dto = self.fabrica_transaccion.crear_objeto(
            transaccion, MapeadorTransaccion())
        db.session.add(transaccion_dto)
        db.session.commit()

    def actualizar(self, transaccion: Transaccion):
        transaccion_dto = db.session.query(TransaccionDTO).filter_by(
            id=str(transaccion._id)).one()
        transaccion_dto.nombre = transaccion.nombre
        transaccion_dto.identificacion = transaccion.identificacion
        transaccion_dto.pais = transaccion.pais
        transaccion_dto.tipo = transaccion.tipo
        transaccion_dto.tipoPersona = transaccion.tipoPersona
        db.session.commit()
