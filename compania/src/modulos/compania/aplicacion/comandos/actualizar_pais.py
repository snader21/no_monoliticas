from src.modulos.compania.dominio.reglas import PaisesValidos
from src.modulos.compania.dominio.repositorios import RepositorioCompanias
from src.seedwork.infraestructura import utils
from .base import CrearCompaniaBaseHandler
from src.modulos.compania.infraestructura.dto import Compania
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pydispatch import dispatcher
@dataclass
class ActualizarPais(Comando):
    _id: str
    nuevo_pais: str


class ActualizarPaisHandler(CrearCompaniaBaseHandler):

    def handle(self, comando: ActualizarPais):
        print(f"Actualizando el pais a {comando.nuevo_pais}")
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        self.fabrica_compania.validar_regla(PaisesValidos(comando.nuevo_pais))
        compania = repositorio.obtener_por_id(comando._id)
        compania.pais = comando.nuevo_pais
        repositorio.actualizar(compania)
        dispatcher.send(signal='PaisActualizadoDominio', evento=compania)


@comando.register(ActualizarPais)
def ejecutar_comando_actualizar_pais(comando: ActualizarPais):
    handler = ActualizarPaisHandler()
    handler.handle(comando)
