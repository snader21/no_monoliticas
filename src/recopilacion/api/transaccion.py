from flask_restful import Resource


def anadir_endpoint_transaccion(api):
    api.add_resource(TransaccionEndPoints, '/transacciones')


class TransaccionEndPoints(Resource):
    def post(self):
        return "hello world"
