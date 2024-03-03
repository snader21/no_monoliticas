from compania.src.modulos.compania.aplicacion.mapeadores import MapeadorCompania
from compania.src.modulos.compania.dominio.repositorios import RepositorioCompanias
from .base import CrearCompaniaBaseHandler
from compania.src.modulos.compania.infraestructura.dto import Compania
from compania.src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from compania.src.seedwork.aplicacion.comandos import ejecutar_commando as comando


@dataclass
class CrearCompania(Comando):
    tipoPersona: str
    nombre: str
    tipo: str
    pais: str
    identificacion: str

class CrearCompaniaHandler(CrearCompaniaBaseHandler):

    def handle(self, comando: CrearCompania):
        print(f"Agregando la compañia")
        compania_dto = Compania(tipoPersona=comando.tipoPersona, 
                               nombre=comando.nombre, 
                               tipo=comando.tipo, 
                               pais=comando.pais, 
                               identificacion=comando.identificacion)

        compania: Compania = self.fabrica_compania.crear_objeto(compania_dto, MapeadorCompania())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        repositorio.agregar(compania)       


@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)
