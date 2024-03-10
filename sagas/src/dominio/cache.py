from dataclasses import dataclass
from src.dominio.objetos_valor import TipoTransaccion

@dataclass
class CompaniaCache():
    id: str
    tipo_persona: str
    nombre: str
    tipo: str
    pais: str
    identificacion: str

@dataclass
class PropiedadCache():
    id: str
    compania_duena: str
    compania_arrendataria: str
    direccion: str
    tamano: int
    pais_ubicacion: str
    latitud: str
    longitud: str

@dataclass
class TransaccionCache():
    id: str
    descripcion: str
    tipo: TipoTransaccion
    compania_origen: str
    compania_destino: str
    pais_transaccion_origen: str
    valor_transaccion_subtotal: int
    impuesto_transaccion: int
    valor_transaccion_total: int
    id_propiedad: str

@dataclass
class CrearTransaccionCache():
    compania_origen: CompaniaCache
    compania_destino: CompaniaCache
    propiedad: PropiedadCache
    transaccion: TransaccionCache
    id_correlacion = str