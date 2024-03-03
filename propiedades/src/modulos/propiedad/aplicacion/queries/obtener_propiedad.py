from src.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from src.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedad


@dataclass
class ObtenerPropiedad(Query):
    id: str


class ObtenerPropiedadHandler(PropiedadQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedades.__class__)
        propiedad = self._fabrica_propiedad.crear_objeto(
            repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=propiedad)


@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)
