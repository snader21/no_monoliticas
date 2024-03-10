from src.infraestructura.schema.v1.comandos import ComandoCompensarPropiedadPayload
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pydispatch import dispatcher


@dataclass
class CompensarPropiedad(Comando):
    id_propiedad: str

class CompensarPropiedadHandler():

    def handle(self, comando: CompensarPropiedad):
        print(f"Compensando la propiedad: {comando.id_propiedad}")
        compania_dto = ComandoCompensarPropiedadPayload(id_propiedad=comando.id_propiedad)
        
        dispatcher.send(signal='CompensarPropiedad', evento=compania_dto)


@comando.register(CompensarPropiedad)
def ejecutar_comando_compensar_propiedad(comando: CompensarPropiedad):
    handler = CompensarPropiedadHandler()
    handler.handle(comando)