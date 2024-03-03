from pulsar.schema import *

class PropiedadActualizadaPayload(Record):
    id_propiedad = String()
    direccion = String()

class UbicacionActualizadaPayload(Record):
    id_propiedad=String() 
    latitud=String()
    longitud=String()
    estrato=String()


     

