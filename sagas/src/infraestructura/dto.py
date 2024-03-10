import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src import db


class Saga(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    comando = db.Column(db.String(100))
    evento = db.Column(db.String(100))
    error = db.Column(db.String(100))
    compensacion = db.Column(db.String(100))
    exitoso = db.Column(db.Boolean)
