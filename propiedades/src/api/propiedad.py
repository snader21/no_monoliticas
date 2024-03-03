import json
from flask import Response, request
from flask_restful import Resource
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.seedwork.aplicacion.queries import ejecutar_query
from src.seedwork.dominio.excepciones import ExcepcionDominio
from src.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from src.modulos.propiedad.aplicacion.comandos.crear_propiedad import CrearPropiedad
from src.modulos.propiedad.aplicacion.queries.obtener_propiedad import ObtenerPropiedad


def anadir_endpoint_propiedad(api):
    api.add_resource(PropiedadEndPoints, '/propiedades/')
    api.add_resource(PropiedadIdEndPoints, '/propiedades/<id_propiedad>')


class PropiedadEndPoints(Resource):
    def post(self):
        try:
            propiedad_dict = request.json
            map_propiedad = MapeadorPropiedadDTOJson()
            propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

            comando = CrearPropiedad(propiedad_dto.compania_duena, propiedad_dto.compania_arrendataria,
                                     propiedad_dto.direccion, propiedad_dto.tamano, propiedad_dto.pais_ubicacion, propiedad_dto.latitud, propiedad_dto.longitud)
            ejecutar_commando(comando)
            return {'message': "Propiedad creada", "status": 201}
        except ExcepcionDominio as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


class PropiedadIdEndPoints(Resource):
    def get(self, id_propiedad):
        if id_propiedad is None:
            return Response(json.dumps(dict(error="debe proporcionar el id de la propiedad a obtener")), status=400, mimetype='application/json')
        query_resultado = ejecutar_query(ObtenerPropiedad(id=id_propiedad))
        map_reserva = MapeadorPropiedadDTOJson()
        return map_reserva.dto_a_externo(query_resultado.resultado)
