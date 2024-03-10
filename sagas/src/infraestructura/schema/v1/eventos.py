from pulsar.schema import *

class CompaniaCreadaPayload(Record):
    id_compania = String()
    id_correlacion = String()
    tipo = String()

class CompaniaFallidaPayload(Record):
    id_compania = String()
    id_correlacion = String()
    tipo = String()

class PropiedadCreadaPayload(Record):
    ...

class PropiedadFallidaPayload(Record):
    ...

class TransaccionCreadaPayload(Record):
    ...

class TransaccionFallidaPayload(Record):
    ...
