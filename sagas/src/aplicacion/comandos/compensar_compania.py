from src.infraestructura.schema.v1.comandos import ComandoCompensarCompaniaPayload
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pydispatch import dispatcher


@dataclass
class CompensarCompania(Comando):
    id_compania: str

class CompensarCompaniaHandler():

    def handle(self, comando: CompensarCompania):
        print(f"Compensando la compañia: {comando.id_compania}")
        compania_dto = ComandoCompensarCompaniaPayload(id_compania=comando.id_compania)
        
        dispatcher.send(signal='CompensarCompania', evento=compania_dto)


@comando.register(CompensarCompania)
def ejecutar_comando_compensar_compania(comando: CompensarCompania):
    handler = CompensarCompaniaHandler()
    handler.handle(comando)