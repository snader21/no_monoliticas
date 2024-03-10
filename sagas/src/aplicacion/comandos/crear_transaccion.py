from src.infraestructura.schema.v1.comandos import ComandoCrearTransaccionPayload
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pydispatch import dispatcher


@dataclass
class CrearTransaccion(Comando):
    descripcion: str
    tipo: str
    compania_origen: str
    compania_destino: str
    pais_transaccion_origen: str
    valor_transaccion_subtotal: int
    id_propiedad: str
    id_correlacion: str

class CrearTransaccionHandler():

    def handle(self, comando: CrearTransaccion):
        print(f"Agregando la transaccion")
        transaccion_dto = ComandoCrearTransaccionPayload(descripcion=comando.descripcion,
                                                         tipo=comando.tipo,
                                                         compania_origen=comando.compania_origen,
                                                         compania_destino=comando.compania_destino,
                                                         pais_transaccion_origen=comando.pais_transaccion_origen,
                                                         valor_transaccion_subtotal=comando.valor_transaccion_subtotal,
                                                         id_propiedad=comando.id_propiedad,
                                                         id_correlacion=comando.id_correlacion)

        print(f"Agregando la transaccion {transaccion_dto}")
        dispatcher.send(signal='CrearTransaccion', evento=transaccion_dto)


@comando.register(CrearTransaccion)
def ejecutar_comando_crear_transaccion(comando: CrearTransaccion):
    handler = CrearTransaccionHandler()
    handler.handle(comando)