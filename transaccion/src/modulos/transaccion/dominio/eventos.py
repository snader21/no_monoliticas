from __future__ import annotations
from dataclasses import dataclass, field
from transaccion.src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class VentaRealizada(EventoDominio):
    id_compania: str = None
    id_propiedad: str = None