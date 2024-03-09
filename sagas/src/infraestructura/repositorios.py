from src import db
from src.dominio.repositorios import RepositorioSaga
from src.dominio.entidades import Saga
from src.dominio.fabricas import FabricaSaga
from src.infraestructura.mapeadores import MapeadorSaga
from .dto import Saga as SagaDTO
from uuid import UUID


class RepositorioSagaPostgress(RepositorioSaga):
    def __init__(self):
        self._fabrica_saga: FabricaSaga = FabricaSaga()

    @property
    def fabrica_saga(self):
        return self._fabrica_saga

    def obtener_por_id(self, id: UUID) -> Saga:
        saga_dto = db.session.query(
            SagaDTO).filter_by(id=str(id)).one()
        return self.fabrica_saga.crear_objeto(saga_dto, MapeadorSaga())

    def agregar(self, saga: Saga):
        saga_dto = self.fabrica_saga.crear_objeto(
            saga, MapeadorSaga())
        db.session.add(saga_dto)
        db.session.commit()

    def actualizar(self, saga: Saga):
        saga_dto = db.session.query(
            SagaDTO).filter_by(id=str(saga._id)).one()
        saga_dto.exitoso = saga.exitoso
        db.session.commit()