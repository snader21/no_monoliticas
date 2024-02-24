from dataclasses import dataclass
from src.recopilacion.modulos.transaccion.aplicacion.comandos.base import CrearTransaccionBaseHandler
from src.recopilacion.modulos.transaccion.aplicacion.dto import TransaccionDTO
from src.recopilacion.modulos.transaccion.aplicacion.mapeadores import MapeadorTransaccion
from src.recopilacion.modulos.transaccion.dominio.entidades import Transaccion
from src.recopilacion.modulos.transaccion.infraestructura.repositorios import RepositorioTransacciones
from src.recopilacion.seedwork.aplicacion.comandos import Comando
from src.recopilacion.seedwork.aplicacion.comandos import ejecutar_commando as comando


@dataclass
class CrearTransaccion(Comando):
    descripcion: str
    tipo: str
    compania_origen: str
    compania_destino: str
    pais_transaccion_origen: str
    valor_transaccion_subtotal: int


class CrearTransaccionHandler(CrearTransaccionBaseHandler):

    def handle(self, comando: CrearTransaccion):
        transaccion_dto = TransaccionDTO(
            descripcion=comando.descripcion,
            tipo=comando.tipo,
            compania_origen=comando.compania_origen,
            compania_destino=comando.compania_destino,
            pais_transaccion_origen=comando.pais_transaccion_origen,
            valor_transaccion_subtotal=comando.valor_transaccion_subtotal
        )

        transaccion: Transaccion = self.fabrica_transaccion.crear_objeto(
            transaccion_dto, MapeadorTransaccion())
        transaccion.crear_transaccion(transaccion)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        repositorio.agregar(transaccion)


@comando.register(CrearTransaccion)
def ejecutar_comando_crear_transaccion(comando: CrearTransaccion):
    handler = CrearTransaccionHandler()
    handler.handle(comando)
