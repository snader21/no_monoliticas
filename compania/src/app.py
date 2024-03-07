import os

from flask_restful import Api

from compania.src import create_app, db
from compania.src.modulos.compania.infraestructura.dto import Compania
from compania.src.api.compania import anadir_endpoint_compania
def comenzar_consumidor():
    import threading
    import src.modulos.compania.infraestructura.consumidores as cliente
    # Suscripción a eventos
    threading.Thread(target=cliente.suscribirse_a_comando_creacion).start()
    threading.Thread(target=cliente.suscribirse_a_comando_eliminacion).start()

app = create_app('development')
app.app_context().push()
db.create_all()
api = Api(app)
anadir_endpoint_compania(api)
comenzar_consumidor()
