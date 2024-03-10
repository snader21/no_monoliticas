from pulsar.schema import *

class CompaniaCreadaPayload(Record):
    id_compania = String()
    id_correlacion = String()
    tipo = String()

class CompaniaErrorPayload(Record):
    id_compania = String()
    id_correlacion = String()
    tipo = String()

