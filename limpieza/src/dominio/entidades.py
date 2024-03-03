from __future__ import annotations
from seedwork.dominio.entidades import AgregacionRaiz
import src.dominio.objetos_valor as ov
from dataclasses import dataclass, field
import random


@dataclass
class Propiedad(AgregacionRaiz):
    direccion: str = field(hash=True, default=None)
    tamanio: str = field(hash=True, default=None)
    compania_duenia: str = field(hash=True, default=None)
    compania_arrendataria: str = field(hash=True, default=None)
    ubcacion_geografica: ov.UbicacionGeografica = field(hash=True, default=None)
    estrato: str = field(hash=True, default=None)


    def crear_propiedad(self, propiedad: Propiedad):
        self.direccion = propiedad.direccion
        self.tamanio = propiedad.tamanio
        self.compania_duenia = propiedad.compania_duenia
        self.compania_arrendataria = propiedad.compania_arrendataria
        self.ubicacion_geografica = propiedad.ubcacion_geografica
        self.estrato = propiedad.estrato
        self.machingLearning()


    def machingLearning(self):
       if(self.ubicacion_geografica == ''):
           self.calcular_ubicacion_geofrafica(self.direccion)
       if(self.estrato == ''):
           self.calcular_estrato()


    def calcular_ubicacion_geofrafica(self, direccion):    
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