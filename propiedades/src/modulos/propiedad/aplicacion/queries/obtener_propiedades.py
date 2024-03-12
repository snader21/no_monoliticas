from src.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from src.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedad
import uuid


@dataclass
class ObtenerPropiedades(Query):
    pass

class ObtenerPropiedadesHandler(PropiedadQueryBaseHandler):
    def handle(self, query: ObtenerPropiedades) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedades.__class__)
        companias = [self.fabrica_propiedad.crear_objeto(transaccion, MapeadorPropiedad()) for transaccion in repositorio.obtener_todos()]
        return QueryResultado(resultado=companias)

@query.register(ObtenerPropiedades)
def ejecutar_query_obtener_reserva(query: ObtenerPropiedades):
    handler = ObtenerPropiedadesHandler()
    return handler.handle(query)
