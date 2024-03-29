from src.dominio.fabricas import FabricaPropiedad
from src.dominio.entidades import Propiedad
from src.seedwork.aplicacion.servicios import Servicio


class ServicioPropiead(Servicio):
    def __init__(self):
        self._fabrica_Propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedades(self):
        return self.fabrica_propiedades

    
    def maching_learning(self, idPropiedad, direccion):
        propiedad: Propiedad = Propiedad()
        propiedad.id = idPropiedad
        propiedad.direccion = direccion
        propiedad.ubcacion_geografica = ''
        propiedad.estrato = ''
        propiedad.machingLearning()
        
