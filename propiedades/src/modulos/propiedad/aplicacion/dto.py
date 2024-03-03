from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadDTO(DTO):
    compania_duena: str = field(default_factory=str)
    compania_arrendataria: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    tamano: int = field(default_factory=int)
    pais_ubicacion: str = field(default_factory=str)
    latitud: float = field(default_factory=float)
    longitud: float = field(default_factory=float)
