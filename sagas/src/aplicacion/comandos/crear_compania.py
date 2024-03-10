from src.infraestructura.schema.v1.comandos import ComandoCrearCompaniaPayload
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pydispatch import dispatcher


@dataclass
class CrearCompania(Comando):
    tipoPersona: str
    nombre: str
    tipo: str
    pais: str
    identificacion: str
    id_correlacion: str

class CrearCompaniaHandler():

    def handle(self, comando: CrearCompania):
        print(f"Agregando la compañia")
        compania_dto = ComandoCrearCompaniaPayload(tipoPersona=comando.tipoPersona, 
                               nombre=comando.nombre, 
                               tipo=comando.tipo, 
                               pais=comando.pais, 
                               identificacion=comando.identificacion,
                               id_correlacion=comando.id_correlacion)
        print(f"Agregando la compañia {compania_dto}")
        dispatcher.send(signal='CrearCompania', evento=compania_dto)


@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)