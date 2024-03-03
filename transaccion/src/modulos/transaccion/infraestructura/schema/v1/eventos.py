from pulsar.schema import *

class VentaRealizadaPayload(Record):
    id_propiedad = String()
    compania_destino_id = String()
