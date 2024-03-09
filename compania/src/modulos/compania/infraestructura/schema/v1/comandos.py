from pulsar.schema import *
from dataclasses import dataclass, field

class ComandoCrearCompaniaPayload(Record):
    tipoPersona=String()
    nombre=String()
    tipo=String()
    pais=String()
    identificacion=String()
    id_correlacion = String()

class ComandoBorrarCompaniaPayload(Record):
    id_compania = String()