from transaccion.src.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from transaccion.src.seedwork.aplicacion.queries import ejecutar_query as query
from transaccion.src.modulos.transaccion.infraestructura.repositorios import RepositorioTransacciones
from dataclasses import dataclass
from .base import TransaccionQueryBaseHandler
from transaccion.src.modulos.transaccion.aplicacion.mapeadores import MapeadorTransaccion
import uuid


@dataclass
class ObtenerTransacciones(Query):
    pass

class ObtenerTransaccionesHandler(TransaccionQueryBaseHandler):
    def handle(self, query: ObtenerTransacciones) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        companias = [self.fabrica_transaccion.crear_objeto(transaccion, MapeadorTransaccion()) for transaccion in repositorio.obtener_todos()]
        return QueryResultado(resultado=companias)

@query.register(ObtenerTransacciones)
def ejecutar_query_obtener_reserva(query: ObtenerTransacciones):
    handler = ObtenerTransaccionesHandler()
    return handler.handle(query)
