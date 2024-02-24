from flask import request
from flask_restful import Resource


def anadir_endpoint_transaccion(api):
    api.add_resource(TransaccionEndPoints, '/transacciones')
    api.add_resource(TransaccionIdEndPoints, '/transacciones/<id_compania>')


class TransaccionEndPoints(Resource):
    def post(self):
        try:
            transaccion_dict = request.json
            comando = CrearCompania(**compania_dict)
            ejecutar_commando(comando)
            return {'message': "Compania creada", "status": 202}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


class TransaccionIdEndPoints(Resource):
    def post(self):
        return "hello world"