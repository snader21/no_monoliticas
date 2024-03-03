from __future__ import annotations
from src.seedwork.dominio.entidades import AgregacionRaiz
import src.dominio.objetos_valor as ov
from dataclasses import dataclass, field
import random
from pydispatch import dispatcher


@dataclass
class Propiedad(AgregacionRaiz):
    id: str = field(hash=True, default=None)
    direccion: str = field(hash=True, default=None)
    ubicacion_geografica: ov.UbicacionGeografica = field(hash=True, default=None)
    estrato: str = field(hash=True, default=None)


    def crear_propiedad(self, propiedad: Propiedad):
        self.id = propiedad.id
        self.direccion = propiedad.direccion
        self.ubicacion_geografica = propiedad.ubicacion_geografica
        self.estrato = propiedad.estrato
        self.machingLearning()


    def machingLearning(self):
        print('Calculando ubicacion geografica y estrato')
        print(self.ubicacion_geografica)
        if(self.ubicacion_geografica == '' or self.ubicacion_geografica is None):
           self.calcular_ubicacion_geofrafica()
        if(self.estrato == '' or self.estrato is None):
           self.calcular_estrato()   
        print("EVENTOO")
        print(self)
        dispatcher.send(signal='PropiedadActualizadaDominio', evento=self)


    def calcular_ubicacion_geofrafica(self):    
        # Generar latitud y longitud
        ubicacion: ov.UbicacionGeografica = ov.UbicacionGeografica()
        ubicacion.latitud = f"{random.randint(0, 180)}° {random.randint(0, 59)}' {random.randint(0, 59)}″"
        ubicacion.longitud = f"{random.randint(0, 180)}° {random.randint(0, 59)}' {random.randint(0, 59)}″"
        self.ubicacion_geografica = ubicacion

    def calcular_estrato(self):
        #Calcular estrato
        self.estrato = int(random.uniform(1, 6))