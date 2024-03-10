from pulsar.schema import *

class ComandoCrearCompaniaPayload(Record):
    tipoPersona=String()
    nombre=String()
    tipo=String()
    pais=String()
    identificacion=String()
    id_correlacion = String()

class ComandoCompensarCompaniaPayload(Record):
    id_compania = String()