import os

from flask_restful import Api
from src import create_app
from src.aplicacion.transaction import anadir_endpoint_compania

def comenzar_consumidor():
    import threading
    import src.infraestructura.consumidores as cliente
    threading.Thread(target=cliente.suscribirse_a_compania_creada).start()
    threading.Thread(target=cliente.suscribirse_a_compania_fallida).start()
    threading.Thread(target=cliente.suscribirse_a_propiedad_creada).start()
    threading.Thread(target=cliente.suscribirse_a_transaccion_creada).start()

app = create_app()
app.app_context().push()
api = Api(app)
anadir_endpoint_compania(api)
comenzar_consumidor()