from src.recopilacion.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.recopilacion.seedwork.aplicacion.comandos import ejecutar_commando as comando


@dataclass
class ActualizarPais(Comando):
    nuevo_pais: str


class ActualizarPaisHandler():

    def handle(self, comando: ActualizarPais):

        print(f"Actualizando el pais a {comando.nuevo_pais}")


@comando.register(ActualizarPais)
def ejecutar_comando_actualizar_pais(comando: ActualizarPais):
    handler = ActualizarPaisHandler()
    handler.handle(comando)
