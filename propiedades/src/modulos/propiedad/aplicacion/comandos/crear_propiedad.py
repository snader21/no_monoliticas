from dataclasses import dataclass, field
from .base import CrearPropiedadBaseHandler
from src.modulos.propiedad.aplicacion.dto import PropiedadDTO
from src.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedad
from src.modulos.propiedad.dominio.entidades import Propiedad
from src.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from src.seedwork.aplicacion.comandos import Comando
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando


@dataclass
class CrearPropiedad(Comando):
    compania_duena: str
    compania_arrendataria: str
    direccion: str
    tamano: int
    pais_ubicacion: str
    latitud: float
    longitud: float


class CrearPropiedadHandler(CrearPropiedadBaseHandler):

    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
            compania_duena=comando.compania_duena,
            compania_arrendataria=comando.compania_arrendataria,
            direccion=comando.direccion,
            tamano=comando.tamano,
            pais_ubicacion=comando.pais_ubicacion,
            latitud=comando.latitud,
            longitud=comando.longitud
        )

        propiedad: Propiedad = self.fabrica_propiedad.crear_objeto(
            propiedad_dto, MapeadorPropiedad())
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedades.__class__)
        repositorio.agregar(propiedad)


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
