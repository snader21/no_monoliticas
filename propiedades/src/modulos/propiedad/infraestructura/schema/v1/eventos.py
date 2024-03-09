from pulsar.schema import *


class VentaRealizadaPayload(Record):
    id_propiedad = String()
    compania_destino_id = String()


class UbicacionActualizadaPayload(Record):
    id_propiedad = String()
    latitud = String()
    longitud = String()
    estrato = String()


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    direccion = String()

class CreacionDePropiedadFallidaPayload(Record):
    id_correlacion = String()