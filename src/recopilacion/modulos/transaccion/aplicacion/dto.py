from dataclasses import dataclass, field
from src.recopilacion.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class TransaccionDTO(DTO):
    descripcion: field(default_factory=str)
    tipo: field(default_factory=str)
    compania_origen: field(default_factory=str)
    compania_destino: field(default_factory=str)
    pais_transaccion_origen: field(default_factory=str)
    valor_transaccion_subtotal: field(default_factory=int)