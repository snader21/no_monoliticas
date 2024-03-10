from src.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.transaccion.infraestructura.repositorios import RepositorioTransacciones
from dataclasses import dataclass
from .base import TransaccionQueryBaseHandler
from src.modulos.transaccion.aplicacion.mapeadores import MapeadorTransaccion
import uuid


@dataclass
class ObtenerTransaccionPorId(Query):
    id: str

class ObtenerTransaccionPorIdHandler(TransaccionQueryBaseHandler):
    def handle(self, query: ObtenerTransaccionPorId) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        transaccion = self.fabrica_transaccion.crear_objeto(
            repositorio.obtener_por_id(query.id), MapeadorTransaccion())
        return QueryResultado(resultado=transaccion)

@query.register(ObtenerTransaccionPorId)
def ejecutar_query_obtener_reserva(query: ObtenerTransaccionPorId):
    handler = ObtenerTransaccionPorIdHandler()
    return handler.handle(query)
