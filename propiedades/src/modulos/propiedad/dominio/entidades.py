from __future__ import annotations
from dataclasses import dataclass, field

from src.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Propiedad(AgregacionRaiz):
    compania_duena: str = field(hash=True, default=None)
    compania_arrendataria: str = field(hash=True, default=None)
    direccion: str = field(hash=True, default=None)
    tamano: int = field(hash=True, default=None)
    pais_ubicacion: str = field(hash=True, default=None)
    latitud: float = field(hash=True, default=None)
    longitud: float = field(hash=True, default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.compania_duena = propiedad.compania_duena
        self.compania_arrendataria = propiedad.compania_arrendataria
        self.direccion = propiedad.direccion
        self.tamano = propiedad.tamano
        self.pais_ubicacion = propiedad.pais_ubicacion

    def actualizar_compania_duena(self, nueva_compania: str):
        self.compania_duena = nueva_compania

    def actualizar_datos_geograficos(self, latitud: float, longitud: float):
        self.latitud = latitud
        self.longitud = longitud
