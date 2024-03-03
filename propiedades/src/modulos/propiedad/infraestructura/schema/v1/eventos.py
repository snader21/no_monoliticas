from pulsar.schema import *


class TransaccionCreadaPayload():
    id_propiedad = String()
    compania_destino_id = String()


class DatosGeograficosActualizadosPayload():
    id_propiedad = String()
    latitud = Float()
    longitud = Float()
