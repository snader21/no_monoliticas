from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime


@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad: str = None
    direccion: str = None
