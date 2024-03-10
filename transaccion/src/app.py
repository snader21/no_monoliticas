import os

from flask_restful import Api

from src import create_app, db
from src.modulos.transaccion.infraestructura.dto import Transaccion
from src.api.transaccion import anadir_endpoint_transaccion


def comenzar_consumidor():
    import threading
    import src.modulos.transaccion.infraestructura.consumidores as cliente
    # Suscripción a eventos
    threading.Thread(target=cliente.suscribirse_a_eventos).start()
    threading.Thread(target=cliente.suscribirse_a_comando_creacion).start()
    threading.Thread(target=cliente.suscribirse_a_comando_eliminacion).start()


app = create_app('development')
app.app_context().push()
db.create_all()
api = Api(app)
anadir_endpoint_transaccion(api)
comenzar_consumidor()
