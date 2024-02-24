import enum
import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.recopilacion import db
print(db)


class TipoTransaccion(enum.Enum):
    VENTA = "VENTA"
    ARRIENDO = "ARRIENDO"


class EnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.value


class Transaccion(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    descripcion = db.Column(db.String(100))
    tipo = db.Column(db.Enum(TipoTransaccion))
    compania_origen = db.Column(UUID(as_uuid=True))
    compania_destino = db.Column(UUID(as_uuid=True))
    pais_compania_origen = db.Column(db.String(100))
    valor_transaccion_subtotal = db.Column(db.Integer)
    impuesto_transaccion = db.Column(db.Integer)
    valor_transaccion_total = db.Column(db.Integer)


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
