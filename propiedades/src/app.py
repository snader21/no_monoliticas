import os

from flask_restful import Api

from src import create_app, db
from src.api.propiedad import anadir_endpoint_propiedad


def comenzar_consumidor():
    import threading
    import src.modulos.propiedad.infraestructura.consumidores as cliente
    # Suscripción a eventos
    threading.Thread(
        target=cliente.suscribirse_a_eventos_de_transacciones).start()
    # threading.Thread(target=cliente.suscribirse_a_eventos_de_limpieza).start()


app = create_app('development')
app.app_context().push()
db.create_all()
api = Api(app)
anadir_endpoint_propiedad(api)
comenzar_consumidor()
