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

class ComandoCrearPropiedadPayload(Record):
    compania_duena = String()
    compania_arrendataria = String()
    direccion = String()
    tamano = Integer()
    pais_ubicacion = String()
    id_correlacion = String()

class ComandoCompensarPropiedadPayload(Record):
    id_propiedad = String()


class ComandoCrearTransaccionPayload(Record):
    descripcion= String()
    tipo= String()
    compania_origen= String()
    compania_destino= String()
    pais_transaccion_origen= String()
    valor_transaccion_subtotal= Integer()
    id_propiedad= String()
    id_correlacion = String()