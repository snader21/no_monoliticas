import json
from flask import Response, request
from flask_restful import Resource
from src.aplicacion.comandos.ejecutar_saga import EjecutarSaga
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.seedwork.dominio.excepciones import ExcepcionDominio

def anadir_endpoint_compania(api):
    api.add_resource(TransactionEndPoints, '/transaccion/')


class TransactionEndPoints(Resource):
    def post(self):
        try:
            transaccion_dict = request.json
            comando = EjecutarSaga(**transaccion_dict)
            ejecutar_commando(comando)
            return {'message': "Transaccion creada", "status": 202}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')