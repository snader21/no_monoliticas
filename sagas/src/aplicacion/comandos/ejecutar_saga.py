from ast import List
from dataclasses import dataclass
from src.aplicacion.comandos.crear_compania import CrearCompania
from src.aplicacion.comandos.compensar_compania import CompensarCompania
from src.seedwork.aplicacion.comandos import Comando
from src.dominio.objetos_valor import TipoTransaccion
from src.seedwork.aplicacion.comandos import Comando
from src.seedwork.aplicacion.comandos import ejecutar_commando
from pydispatch import dispatcher
import uuid
from src.seedwork.aplicacion.sagas import CoordinadorOrquestacion, TransaccionSaga, Inicio, Fin
from src.dominio.cache import CrearTransaccionCache, CompaniaCache, PropiedadCache, TransaccionCache
from localStoragePy import localStoragePy
import json
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class Compania():
    tipo_persona: str
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
    pais_transaccion_origen: str
    valor_transaccion_subtotal: int
    impuesto_transaccion: int
    valor_transaccion_total: int

@dataclass
class EjecutarSaga(Comando):
    compania_origen: Compania
    compania_destino: Compania
    propiedad: Propiedad
    transaccion: Transaccion

class EjecutarSagaHandler():

    local_storage = localStoragePy('saga', 'json')

    def handle(self, comando: EjecutarSaga):
        id_correlacion = uuid.uuid4()
        transaccionCache_json = json.dumps(comando, default=lambda o: o.__dict__)
        self.local_storage.setItem(str(id_correlacion),transaccionCache_json)
        comando = CrearCompania(id_correlacion=str(id_correlacion),  
                        tipoPersona=comando.compania_origen['tipo_persona'],
                        nombre=comando.compania_origen['nombre'],
                        tipo=comando.compania_origen['tipo'],
                        pais=comando.compania_origen['pais'],
                        identificacion=comando.compania_origen['identificacion'])
    
        ejecutar_commando(comando)


@comando.register(EjecutarSaga)
def ejecutar_comando_crear_propiedad(comando: EjecutarSaga):
    handler = EjecutarSagaHandler()
    handler.handle(comando)