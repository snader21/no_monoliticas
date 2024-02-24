from __future__ import annotations
from dataclasses import dataclass, field
from src.recopilacion.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class PaisActualizado(EventoDominio):
    id_compania: str = None
    pais_nuevo: str = None