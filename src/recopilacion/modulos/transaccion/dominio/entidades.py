from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import src.recopilacion.modulos.transaccion.dominio.objetos_valor as ov
# from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from src.recopilacion.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Transaccion(AgregacionRaiz):

    descripcion: str = field(hash=True, default=None)
    tipo: ov.TipoTransaccion = field(hash=True, default=None)
    compania_origen: str = field(hash=True, default=None)
    compania_destino: str = field(hash=True, default=None)
    pais_transaccion_origen: str = field(hash=True, default=None)
    valor_transaccion_subtotal: int = field(hash=True, default=None)
    impuesto_transaccion: int = field(hash=True, default=None)
    valor_transaccion_total: int = field(hash=True, default=None)

    def crear_transaccion(self, transaccion: Transaccion):

        self.descripcion = transaccion.descripcion
        self.tipo = transaccion.tipo
        self.compania_origen = transaccion.compania_origen
        self.compania_destino = transaccion.compania_destino
        self.pais_transaccion_origen = transaccion.pais_transaccion_origen
        self.valor_transaccion_subtotal = transaccion.valor_transaccion_subtotal
        self.impuesto_transaccion = transaccion.impuesto_transaccion
        self.valor_transaccion_total = transaccion.valor_transaccion_total

        if self.pais_transaccion_origen == "Colombia":
            self.impuesto_transaccion = self.valor_transaccion_subtotal * 0.19
        elif self.pais_transaccion_origen == "Ecuador":
            self.impuesto_transaccion = self.valor_transaccion_subtotal * 0.20
        elif self.pais_transaccion_origen == "Peru":
            self.impuesto_transaccion = self.valor_transaccion_subtotal * 0.21

        self.valor_transaccion_total = self.valor_transaccion_subtotal + \
            self.impuesto_transaccion

    def actualizar_impuesto(self, nuevo_pais: str):
        pass
        # self.estado = ov.EstadoReserva.APROBADA

        # self.agregar_evento(ReservaAprobada(self.id, self.fecha_actualizacion))
