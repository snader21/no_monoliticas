"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import compania.src.modulos.compania.dominio.objetos_valor as ov
# from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from compania.src.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Compania(AgregacionRaiz):
    tipoPersona: ov.TipoPersona = field(hash=True, default=None)
    nombre: str = field(hash=True, default=None)
    tipo: ov.TipoCompania = field(hash=True, default=None)
    pais: str = field(hash=True, default=None)
    identificacion: str = field(hash=True, default=None)

    def crear_compania(self, compania: Compania):
        pass
        # self.id_cliente = reserva.id_cliente
        # self.estado = reserva.estado
        # self.itinerarios = reserva.itinerarios

        # self.agregar_evento(ReservaCreada(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def actualizar_pais(self, nuevo_pais: str):
        pass
        # self.estado = ov.EstadoReserva.APROBADA

        # self.agregar_evento(ReservaAprobada(self.id, self.fecha_actualizacion))