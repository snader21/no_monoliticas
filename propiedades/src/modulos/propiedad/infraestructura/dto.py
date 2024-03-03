import enum
import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src import db


class Propiedad(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    compania_duena = db.Column(UUID(as_uuid=True))
    compania_arrendataria = db.Column(UUID(as_uuid=True))
    direccion = db.Column(db.String(100))
    tamano = db.Column(db.Integer)
    pais_ubicacion = db.Column(db.String(100))
    latitud = db.Column(db.Float, nullable=True)
    longitud = db.Column(db.Float, nullable=True)
