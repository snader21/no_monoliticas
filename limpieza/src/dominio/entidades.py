from __future__ import annotations
from seedwork.dominio.entidades import AgregacionRaiz
import src.dominio.objetos_valor as ov
from dataclasses import dataclass, field
import random
from pydispatch import dispatcher


@dataclass
class Propiedad(AgregacionRaiz):
    id: str = field(hash=True, default=None)
    direccion: str = field(hash=True, default=None)
    ubcacion_geografica: ov.UbicacionGeografica = field(hash=True, default=None)
    estrato: str = field(hash=True, default=None)


    def crear_propiedad(self, propiedad: Propiedad):
        self.id = propiedad.id
        self.direccion = propiedad.direccion
        self.ubicacion_geografica = propiedad.ubcacion_geografica
        self.estrato = propiedad.estrato
        self.machingLearning()


    def machingLearning(self):
        if(self.ubicacion_geografica == ''):
           self.calcular_ubicacion_geofrafica()
        if(self.estrato == ''):
           self.calcular_estrato()   
        dispatcher.send(signal='PropiedadDominio', evento=self)


    def calcular_ubicacion_geofrafica(self):    
        # Generar latitud y longitud
        ubicacion: ov.UbicacionGeografica = {}
        ubicacion.latitud = "{}° {}' {}″".format(self.generar_coordenada())
        ubicacion.longitud = "{}° {}' {}″".format(self.generar_coordenada())
        self.ubicacion_geografica = ubicacion


    def calcular_estrato(self):
        #Calcular estrato
        self.estrato = random.uniform(1, 6)


    def generar_coordenada():
        grados = random.randint(0, 180)
        minutos = random.randint(0, 59)
        segundos = random.randint(0, 59)
        return grados, minutos, segundos