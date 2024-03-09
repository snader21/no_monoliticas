from ast import List
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import Comando
from src.dominio.objetos_valor import TipoTransaccion

@dataclass
class CrearCompania():
    tipoPersona: str
    nombre: str
    tipo: str
    pais: str
    identificacion: str

@dataclass
class Propiedad():
    compania_duena: str
    compania_arrendataria: str
    direccion: str
    tamano: int
    pais_ubicacion: str
    latitud: str
    longitud: str

@dataclass
class Transaccion():
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
class CrearTransaccion(Comando):
    companias: List[CrearCompania]
    propiedad: Propiedad
    transaccion: Transaccion
