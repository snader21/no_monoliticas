from __future__ import annotations
from dataclasses import dataclass, field

from src.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Saga(AgregacionRaiz):
    id_correlacion: str = field(hash=True, default=None)
    comando: str = field(hash=True, default=None)
    evento: str = field(hash=True, default=None)
    error: str = field(hash=True, default=None)
    compensacion: str = field(hash=True, default=None)
    exitoso: bool = field(hash=True, default=None)

    def crear_propiedad(self, saga: Saga):
        self.id_correlacion = saga.id_correlacion
        self.comando = saga.comando
        self.evento = saga.evento
        self.error = saga.error
        self.compensacion = saga.compensacion
        self.exitoso = saga.exitoso