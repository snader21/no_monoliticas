import json
from flask import Response, request
from flask_restful import Resource
from src.recopilacion.modulos.compania.aplicacion.comandos.actualizar_pais import ActualizarPais
from src.recopilacion.modulos.transaccion.aplicacion.comandos.crear_transaccion import CrearTransaccion
# from src.recopilacion.modulos.transaccion.aplicacion.mapeadores import
# from src.recopilacion.modulos.compania.aplicacion.queries.obtener_compania import ObtenerCompania
from src.recopilacion.seedwork.aplicacion.comandos import ejecutar_commando
from src.recopilacion.seedwork.aplicacion.queries import ejecutar_query
from src.recopilacion.seedwork.dominio.excepciones import ExcepcionDominio
from src.recopilacion.modulos.transaccion.aplicacion.mapeadores import MapeadorTransaccionDTOJson


def anadir_endpoint_transaccion(api):
    api.add_resource(TransaccionEndPoints, '/transacciones')
    api.add_resource(TransaccionIdEndPoints, '/transacciones/<id_compania>')


class TransaccionEndPoints(Resource):
    def post(self):
        try:
            transaccion_dict = request.json
            map_transaccion = MapeadorTransaccionDTOJson()
            transaccion_dto = map_transaccion.externo_a_dto(transaccion_dict)

            comando = CrearTransaccion(transaccion_dto.descripcion, transaccion_dto.tipo, transaccion_dto.compania_origen, transaccion_dto.compania_destino,
                                       transaccion_dto.pais_transaccion_origen, transaccion_dto.valor_transaccion_subtotal)
            ejecutar_commando(comando)
            return {'message': "Transaccion creada", "status": 201}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


class TransaccionIdEndPoints(Resource):
    def post(self):
        return "hello world"
