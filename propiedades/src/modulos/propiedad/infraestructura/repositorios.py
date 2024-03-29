""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de compania

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de compania

"""

from src import db
from src.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from src.modulos.propiedad.dominio.entidades import Propiedad
from src.modulos.propiedad.dominio.fabricas import FabricaPropiedad
from src.modulos.propiedad.infraestructura.mapeadores import MapeadorPropiedad
from .dto import Propiedad as PropiedadDTO
from uuid import UUID


class RepositorioPropiedadesPostgress(RepositorioPropiedades):
    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(
            PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedad())
    
    def obtener_todos(self) -> list[Propiedad]:
        transacciones = db.session.query(PropiedadDTO).all()
        return [self.fabrica_propiedad.crear_objeto(transaccion_dto, MapeadorPropiedad()) for transaccion_dto in transacciones]

    def agregar(self, propiedad: Propiedad):
        propiedad_dto: PropiedadDTO = self.fabrica_propiedad.crear_objeto(
            propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)
        db.session.commit()
        return propiedad_dto.id

    def actualizar(self, propiedad: Propiedad):
        propiedad_dto = db.session.query(
            PropiedadDTO).filter_by(id=str(propiedad._id)).one()
        propiedad_dto.compania_duena = propiedad.compania_duena
        propiedad_dto.compania_arrendataria = propiedad.compania_arrendataria
        propiedad_dto.direccion = propiedad.direccion
        propiedad_dto.tamano = propiedad.tamano
        propiedad_dto.pais_ubicacion = propiedad.pais_ubicacion
        propiedad_dto.latitud = propiedad.latitud
        propiedad_dto.longitud = propiedad.longitud
        db.session.commit()

    def eliminar(self, id_propiedad: UUID):
        db.session.query(PropiedadDTO).filter_by(id=str(id_propiedad)).delete()
        db.session.commit()