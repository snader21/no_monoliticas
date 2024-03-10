from src.infraestructura.schema.v1.comandos import ComandoCrearCompaniaPayload, ComandoCrearPropiedadPayload
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pydispatch import dispatcher


@dataclass
class CrearPropiedad(Comando):
    compania_duena: str
    compania_arrendataria: str
    direccion: str
    tamano: int
    pais_ubicacion: str
    latitud: str
    longitud: str

class CrearPropiedadHandler():

    def handle(self, comando: CrearPropiedad):
        print(f"Agregando la propiedad")
        propiedad_dto = ComandoCrearPropiedadPayload(compania_duena=comando.compania_duena,
                                                     compania_arrendataria=comando.compania_arrendataria,
                                                     direccion=comando.direccion,
                                                     tamano=comando.tamano,
                                                     pais_ubicacion=comando.pais_ubicacion,
                                                     latitud=comando.latitud,
                                                     longitud=comando.longitud)
        print(f"Agregando la propiedad {propiedad_dto}")
        dispatcher.send(signal='CrearPropiedad', evento=propiedad_dto)


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_compania(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)