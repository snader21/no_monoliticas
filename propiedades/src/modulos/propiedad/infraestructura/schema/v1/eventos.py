from pulsar.schema import *

class VentaRealizadaPayload(Record):
    id_propiedad = String()
    compania_destino_id = String()


class DatosGeograficosActualizadosPayload(Record):
    id_propiedad = String()
    latitud = Float()
    longitud = Float()


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    direccion = String()
