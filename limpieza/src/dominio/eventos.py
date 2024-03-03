from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from src.dominio.objetos_valor import UbicacionGeografica


@dataclass
class PropiedadActualizada(EventoDominio):
    id_compania: str = None
    ubicacion: UbicacionGeografica = None
    estrato: str = None