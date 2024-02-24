""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Transaccion
from .reglas import CompaniasDiferentes, PaisesValidos, ValorTransaccionPositivo
#from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from src.recopilacion.seedwork.dominio.repositorios import Mapeador
from src.recopilacion.seedwork.dominio.fabricas import Fabrica
from src.recopilacion.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaTransaccion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            transaccion: Transaccion = mapeador.dto_a_entidad(obj)

            self.validar_regla(PaisesValidos(transaccion.pais_transaccion_origen))
            self.validar_regla(CompaniasDiferentes(transaccion.compania_origen, transaccion.compania_destino))
            self.validar_regla(ValorTransaccionPositivo(transaccion.valor_transaccion_subtotal))
            # Agregar mas reglas de ser necesario

            return transaccion