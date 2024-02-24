from src.recopilacion.modulos.compania.aplicacion.mapeadores import MapeadorCompania
from src.recopilacion.modulos.compania.dominio.reglas import PaisesValidos
from src.recopilacion.modulos.compania.dominio.repositorios import RepositorioCompanias
from .base import CrearCompaniaBaseHandler
from src.recopilacion.modulos.compania.infraestructura.dto import Compania
from src.recopilacion.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.recopilacion.seedwork.aplicacion.comandos import ejecutar_commando as comando
@dataclass
class ActualizarPais(Comando):
    _id: str
    nuevo_pais: str


class ActualizarPaisHandler(CrearCompaniaBaseHandler):

    def handle(self, comando: ActualizarPais):
        print(f"Actualizando el pais a {comando.nuevo_pais}")
        repositorio = self.fabrica_repositorio.crear_objeto(MapeadorCompania.__class__)
        self.fabrica_compania.validar_regla(PaisesValidos(comando.nuevo_pais))
        compania = repositorio.obtener_por_id(comando._id)
        compania.pais = comando.nuevo_pais
        repositorio.actualizar(compania)
        


@comando.register(ActualizarPais)
def ejecutar_comando_actualizar_pais(comando: ActualizarPais):
    handler = ActualizarPaisHandler()
    handler.handle(comando)
