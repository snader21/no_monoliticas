"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from src.recopilacion.seedwork.dominio.reglas import ReglaNegocio


class PaisesValidos(ReglaNegocio):

    def __init__(self, pais, mensaje='El pais tiene que ser Colombia, Ecuador o Perú'):
        super().__init__(mensaje)
        self.pais = pais

    def es_valido(self) -> bool:
        paises_validos = ['Colombia', 'Ecuador', 'Peru']
        return self.pais in paises_validos