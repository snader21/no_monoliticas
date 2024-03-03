from pulsar.schema import *

class PaisActualizadoPayload(Record):
    id_compania = String()
    pais_nuevo = String()

class VentaRealizadaPayload(Record):
    id_propiedad = String()
    compania_destino_id = String()