import os

from flask_restful import Api
from src import create_app

def comenzar_consumidor():
    import threading
    import src.infrastructura.consumidores as cliente
    # Suscripción a eventos
    threading.Thread(target=cliente.suscribirse_a_eventos).start()

app = create_app()
app.app_context().push()
api = Api(app)
comenzar_consumidor()