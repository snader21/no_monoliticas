from src.recopilacion.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from src.recopilacion.seedwork.aplicacion.queries import ejecutar_query as query
from src.recopilacion.modulos.compania.infraestructura.repositorios import MapeadorCompania
from dataclasses import dataclass
from .base import CompaniaQueryBaseHandler
from src.recopilacion.modulos.compania.aplicacion.mapeadores import MapeadorCompania
import uuid

@dataclass
class ObtenerCompania(Query):
    id: str

class ObtenerCompaniaHandler(CompaniaQueryBaseHandler):

    def handle(self, query: ObtenerCompania) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(MapeadorCompania.__class__)
        compania =  self._fabrica_compania.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCompania())
        return QueryResultado(resultado=compania)

@query.register(ObtenerCompania)
def ejecutar_query_obtener_reserva(query: ObtenerCompania):
    handler = ObtenerCompaniaHandler()
    return handler.handle(query)