from src.dominio.repositorios import RepositorioSaga
from .base import CrearSagaBaseHandler
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class GuardarSagaLog(Comando):
    _id: str
    comando: str
    evento: str
    error: str
    compensacion: str
    exitoso: bool


class GuardarSagaHandler(CrearSagaBaseHandler):

    def handle(self, comando: GuardarSagaLog):
        print(f"Guardando paso saga log {comando._id}")
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSaga.__class__)
        repositorio.agregar(comando)


@comando.register(GuardarSagaLog)
def ejecutar_comando_actualizar_pais(comando: GuardarSagaLog):
    handler = GuardarSagaHandler()
    handler.handle(comando)
