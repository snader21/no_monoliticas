from pulsar.schema import *
from dataclasses import dataclass, field

class ComandoCrearPropiedadPayload(Record):
    compania_duena = String()
    compania_arrendataria = String()
    direccion = String()
    tamano = Integer()
    pais_ubicacion = String()
    id_correlacion = String()

class ComandoBorrarPropiedadPayload(Record):
    id_propiedad = String()