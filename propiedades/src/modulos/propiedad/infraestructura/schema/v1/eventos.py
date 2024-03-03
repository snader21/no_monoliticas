from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class TransaccionCreadaPayload(Record):
    id_propiedad = String()
    compania_destino_id = String()


class DatosGeograficosActualizadosPayload(Record):
    id_propiedad = String()
    latitud = Float()
    longitud = Float()


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    direccion = String()


class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()
