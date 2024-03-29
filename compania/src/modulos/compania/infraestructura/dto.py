import enum
import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src import db


class TipoCompania(enum.Enum):
    COMPRADOR = "COMPRADOR"
    VENDEDOR = "VENDEDOR"
    ARRENDATARIO = "ARRENDATARIO"
    ARRENDADOR = "ARRENDADOR"

class TipoPersona(enum.Enum):
    NATURAL = "NATURAL"
    JURIDICA = "JURIDICA"

class EnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.value


class Compania(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tipoPersona = db.Column(db.Enum(TipoPersona))
    nombre = db.Column(db.String(100))
    tipo = db.Column(db.Enum(TipoCompania))
    pais = db.Column(db.String(100))
    identificacion = db.Column(db.String(100))


# class OfferBasicSchema(Schema):
#     id = fields.UUID()
#     userId = fields.Str()
#     createdAt = fields.DateTime()


# class OfferDetailedSchema(Schema):
#     id = fields.UUID()
#     postId = fields.UUID()
#     userId = fields.UUID()
#     description = fields.String()
#     size = EnumField()
#     fragile = fields.Boolean()
#     offer = fields.Integer()
#     createdAt = fields.DateTime()
