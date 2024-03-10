from src.seedwork.aplicacion.sagas import CoordinadorOrquestacion, TransaccionSaga, Inicio, Fin
from src.seedwork.aplicacion.comandos import Comando
from src.seedwork.dominio.eventos import EventoDominio
from src.aplicacion.comandos.guardar_saga_log import GuardarSagaLog
from src.aplicacion.comandos.crear_compania import CrearCompania
from localStoragePy import localStoragePy
import json
from src.dominio.cache import CrearTransaccionCache
from src.seedwork.aplicacion.comandos import ejecutar_commando

local_storage = localStoragePy('saga', 'sqlite')

class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self, pasos):
        self.pasos = pasos

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        comando = GuardarSagaLog()

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
    
def ejecutarComandoCompania(id_compania, id_correlacion, tipo):
    cacheTransaccion = local_storage.getItem(id_correlacion)
    # Deserializar el objeto JSON de vuelta a un diccionario
    transaccionCache_dict = json.loads(cacheTransaccion)

    # Reconstruir el objeto original con los valores del diccionario
    transaccionCache = CrearTransaccionCache(**transaccionCache_dict)
    if tipo == "VENDEDOR":
        transaccionCache.compania_origen.id = id_compania
        comando = CrearCompania(id_correlacion= id_correlacion,
                                tipoPersona= transaccionCache.compania_origen.tipoPersona,
                                nombre=transaccionCache.compania_origen.tipoPersona,
                                tipo=transaccionCache.compania_origen.tipo,
                                pais=transaccionCache.compania_origen.pais,
                                identificacion=transaccionCache.compania_origen.identificacion)
        ejecutar_commando(comando)
        transaccionCache_json = json.dumps(transaccionCache, default=lambda o: o.__dict__)
        local_storage.setItem(id_correlacion,transaccionCache_json)
    else:
        transaccionCache.compania_destino.id = id_compania
