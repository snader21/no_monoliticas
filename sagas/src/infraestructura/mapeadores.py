from src.seedwork.dominio.repositorios import Mapeador
from src.dominio.entidades import Saga
from .dto import Saga as SagaDTO


class MapeadorSaga(Mapeador):

    def obtener_tipo(self) -> type:
        return Saga.__class__

    def entidad_a_dto(self, entidad: Saga) -> SagaDTO:
        saga_dto = SagaDTO()
        saga_dto.id = entidad.id
        saga_dto.comando = entidad.comando
        saga_dto.evento = entidad.evento
        saga_dto.error = entidad.error
        saga_dto.compensacion = entidad.compensacion
        saga_dto.exitoso = entidad.exitoso
        return saga_dto

    def dto_a_entidad(self, dto: SagaDTO) -> Saga:
        saga = Saga()
        saga.id = dto.id
        saga.comando = dto.comando
        saga.evento = dto.evento
        saga.error = dto.error
        saga.compensacion = dto.compensacion
        saga.exitoso = dto.exitoso
        return saga