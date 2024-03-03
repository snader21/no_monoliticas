import json
from flask import Response, request
from flask_restful import Resource
from compania.src.modulos.compania.aplicacion.comandos.actualizar_pais import ActualizarPais
from compania.src.modulos.compania.aplicacion.comandos.crear_compania import CrearCompania
from compania.src.modulos.compania.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from compania.src.modulos.compania.aplicacion.queries.obtener_compania import ObtenerCompania
from compania.src.seedwork.aplicacion.comandos import ejecutar_commando
from compania.src.seedwork.aplicacion.queries import ejecutar_query
from compania.src.seedwork.dominio.excepciones import ExcepcionDominio


def anadir_endpoint_compania(api):
    api.add_resource(CompaniaEndPoints, '/companias/')
    api.add_resource(CompaniaIdeEndPoints, '/companias/<id_compania>')


class CompaniaIdeEndPoints(Resource):
    def get(self, id_compania):
        if id_compania is None:
            return Response(json.dumps(dict(error="debe proporcionar el id de la compania a obtener")), status=400, mimetype='application/json')
        query_resultado = ejecutar_query(ObtenerCompania(id=id_compania))
        map_reserva = MapeadorCompaniaDTOJson()
        return map_reserva.dto_a_externo(query_resultado.resultado)
    
    def patch(self, id_compania):
        try:
            compania_dict = request.json
            comando = ActualizarPais(_id=id_compania, nuevo_pais=compania_dict['pais'])
            ejecutar_commando(comando)
            return {'message': "Pais actualizado", "status": 202}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
        

class CompaniaEndPoints(Resource):
    def post(self):
        try:
            compania_dict = request.json
            comando = CrearCompania(**compania_dict)
            ejecutar_commando(comando)
            return {'message': "Compania creada", "status": 202}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    