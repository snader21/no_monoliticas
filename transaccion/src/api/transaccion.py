import json
from flask import Response, request
from flask_restful import Resource
from src.modulos.transaccion.aplicacion.comandos.crear_transaccion import CrearTransaccion
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.seedwork.aplicacion.queries import ejecutar_query
from src.modulos.transaccion.aplicacion.queries.obtener_transacciones import ObtenerTransacciones
from src.modulos.transaccion.aplicacion.queries.obtener_transaccion_por_id import ObtenerTransaccionPorId
from src.seedwork.dominio.excepciones import ExcepcionDominio
from src.modulos.transaccion.aplicacion.mapeadores import MapeadorTransaccionDTOJson


def anadir_endpoint_transaccion(api):
    api.add_resource(TransaccionEndPoints, '/transacciones')
    api.add_resource(TransaccionIdEndPoints, '/transacciones/<id_transaccion>')


class TransaccionEndPoints(Resource):
    def post(self):
        try:
            transaccion_dict = request.json
            map_transaccion = MapeadorTransaccionDTOJson()
            transaccion_dto = map_transaccion.externo_a_dto(transaccion_dict)

            comando = CrearTransaccion(transaccion_dto.descripcion, transaccion_dto.tipo, transaccion_dto.compania_origen, transaccion_dto.compania_destino,
                                       transaccion_dto.pais_transaccion_origen, transaccion_dto.valor_transaccion_subtotal, transaccion_dto.id_propiedad)
            ejecutar_commando(comando)
            return {'message': "Transaccion creada", "status": 201}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
    def get(self):
        query_resultado = ejecutar_query(ObtenerTransacciones())
        map_reserva = MapeadorTransaccionDTOJson()
        return [map_reserva.dto_a_externo(transaccion_dto) for transaccion_dto in query_resultado.resultado]


class TransaccionIdEndPoints(Resource):
    def get(self, id_transaccion):
        if id_transaccion is None:
            return Response(json.dumps(dict(error="debe proporcionar el id de la compania a obtener")), status=400, mimetype='application/json')
        query_resultado = ejecutar_query(ObtenerTransaccionPorId(id=id_transaccion))
        map_reserva = MapeadorTransaccionDTOJson()
        return map_reserva.dto_a_externo(query_resultado.resultado)
