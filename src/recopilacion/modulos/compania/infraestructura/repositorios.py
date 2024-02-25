""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de compania

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de compania

"""

from src.recopilacion import db
from src.recopilacion.modulos.compania.dominio.repositorios import RepositorioCompanias
# from src.recopilacion.modulos.compania.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from src.recopilacion.modulos.compania.dominio.entidades import Compania
from src.recopilacion.modulos.compania.dominio.fabricas import FabricaCompania
from .dto import Compania as CompaniaDTO
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioCompaniasPostgress(RepositorioCompanias):
    def __init__(self):
        self._fabrica_compania: FabricaCompania = FabricaCompania()

    @property
    def fabrica_compania(self):
        return self._fabrica_compania

    def obtener_por_id(self, id: UUID) -> Compania:
        reserva_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_compania.crear_objeto(reserva_dto, MapeadorCompania())
    
    def obtener_por_compania_origen_id(self, id: UUID) -> Compania:
        pass

    def agregar(self, compania: Compania):
        compania_dto = self.fabrica_compania.crear_objeto(compania, MapeadorCompania())
        db.session.add(compania_dto)
        db.session.commit()

    def actualizar(self, compania: Compania):
        print('identificador:' + str(compania._id))
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(compania._id)).one()
        compania_dto.nombre = compania.nombre
        compania_dto.identificacion = compania.identificacion
        compania_dto.pais = compania.pais
        compania_dto.tipo = compania.tipo
        compania_dto.tipoPersona = compania.tipoPersona
        db.session.commit()