from flask_restful import Resource
from src.recopilacion.modulos.compania.aplicacion.comandos.actualizar_pais import ActualizarPais
from src.recopilacion.seedwork.aplicacion.comandos import ejecutar_commando


def anadir_endpoint_compania(api):
    api.add_resource(CompaniaEndPoints, '/companias')


class CompaniaEndPoints(Resource):
    def get(self):
        # 1. Recibir el request
        # 2. Validar el request
        # 3. Ejecutar el comando
        comando = ActualizarPais(nuevo_pais="Colombia")
        ejecutar_commando(comando)
        # 4. Responder al cliente
        return {'message': "Solicitud recibida", "status": 202}
