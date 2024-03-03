
import dataclasses
from seedwork.dominio.eventos import EventoDominio
from src.dominio.objetos_valor import UbicacionGeografica


@dataclasses
class PropiedadActualizada(EventoDominio):
    id_compania: str = None
    ubicacion: UbicacionGeografica = None
    estrato: str = None