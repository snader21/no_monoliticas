from pulsar.schema import *

class PaisActualizadoPayload(Record):
    id_compania = String()
    pais_nuevo = String()

class CreacionDeCompaniaFallidaPayload(Record):
    id_correlacion = String()

class CompaniaCreadaPayload(Record):
    id_compania = String()
    id_correlacion = String()
    tipo = String()