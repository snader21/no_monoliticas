import os

from flask_restful import Api
from src import create_app
from src.aplicacion.transaction import anadir_endpoint_compania

def comenzar_consumidor():
    import threading
    #import src.infrastructura.consumidores as cliente
    # Suscripción a eventos
    #threading.Thread(target=cliente.suscribirse_a_eventos).start()

app = create_app()
app.app_context().push()
api = Api(app)
anadir_endpoint_compania(api)
#comenzar_consumidor()