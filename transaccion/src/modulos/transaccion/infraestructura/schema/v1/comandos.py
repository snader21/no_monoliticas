from pulsar.schema import *
from dataclasses import dataclass, field
from transaccion.src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearReservaPayload(ComandoIntegracion):
    id_usuario = String()


class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()


class ComandoCrearTransaccionPayload(Record):
    descripcion = String()
    tipo = String()
    compania_origen = String()
    compania_destino = String()
    pais_transaccion_origen = String()
    valor_transaccion_subtotal = Integer()
    id_propiedad = String()


class ComandoBorrarTransaccionPayload(Record):
    id_transaccion = String()
