import os

from flask_restful import Api
from . import create_app

app = create_app()
app.app_context().push()
api = Api(app)