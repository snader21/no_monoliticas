from pulsar.schema import *
from dataclasses import dataclass, field

class ComandoCrearCompaniaPayload():
    tipoPersona=String()
    nombre=String()
    tipo=String()
    pais=String()
    identificacion=String()
    id_correlacion = String()

class ComandoBorrarCompaniaPayload():
    id_compania = String()