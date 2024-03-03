from pulsar.schema import *

class PaisActualizadoPayload(Record):
    id_compania = String()
    pais_nuevo = String()
