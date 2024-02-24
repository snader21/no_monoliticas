from pulsar.schema import *
from dataclasses import dataclass, field
from src.recopilacion.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearReservaPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()