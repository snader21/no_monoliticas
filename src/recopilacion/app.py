import os

from flask_restful import Api

from src.recopilacion import create_app, db
from src.recopilacion.modulos.transaccion.infraestructura.dto import Transaccion
from src.recopilacion.modulos.compania.infraestructura.dto import Compania
from src.recopilacion.api.compania import anadir_endpoint_compania
from src.recopilacion.api.transaccion import anadir_endpoint_transaccion

def comenzar_consumidor():
    import threading
    import src.recopilacion.modulos.transaccion.infraestructura.consumidores as cliente
    # Suscripción a eventos
    threading.Thread(target=cliente.suscribirse_a_eventos).start()

app = create_app('development')
app.app_context().push()
db.create_all()
api = Api(app)
anadir_endpoint_compania(api)
anadir_endpoint_transaccion(api)
comenzar_consumidor()
