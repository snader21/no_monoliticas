"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from enum import Enum
from src.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

class TipoPersona(Enum):
    NATURAL = "NATURAL"
    JURIDICA = "JURIDICA"

class TipoCompania(Enum):
    COMPRADOR = "COMPRADOR"
    VENDEDOR = "VENDEDOR"
    ARRENDATARIO = "ARRENDATARIO"
    ARRENDADOR = "ARRENDADOR"

