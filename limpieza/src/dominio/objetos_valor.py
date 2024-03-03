from dataclasses import dataclass, field


class UbicacionGeografica():
    latitud: str = field(hash=True, default=None)
    longitud: str = field(hash=True, default=None)