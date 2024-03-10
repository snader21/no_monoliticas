from pulsar.schema import *

class CompaniaCreadaPayload(Record):
    id_compania = String()
    id_correlacion = String()
    tipo = String()

class CompaniaFallidaPayload(Record):
    id_correlacion = String()

class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    id_correlacion = String()

class PropiedadFallidaPayload(Record):
    ...

class TransaccionCreadaPayload(Record):
    id_transaccion = String()
    id_correlacion = String()

class TransaccionFallidaPayload(Record):
    ...
