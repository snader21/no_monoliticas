from dataclasses import dataclass, field
from src.recopilacion.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CompaniaDTO(DTO):
    tipoPersona: str = field(hash=True, default=None)
    nombre: str = field(hash=True, default=None)
    tipo: str = field(hash=True, default=None)
    pais: str = field(hash=True, default=None)
    identificacion: str = field(hash=True, default=None)