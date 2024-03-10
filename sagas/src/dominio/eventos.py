from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaCreada(EventoDominio):
    ...

class CompaniaError(EventoDominio):
    ...