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
    
class CompaniasDiferentes(ReglaNegocio):

    def __init__(self, compania_origen, compania_destino, mensaje='La compania origen tiene que ser diferente a la compania destino'):
        super().__init__(mensaje)
        self.compania_origen = compania_origen
        self.compania_destino = compania_destino

    def es_valido(self) -> bool:
        return self.compania_origen != self.compania_destino
    
class ValorTransaccionPositivo(ReglaNegocio):

    def __init__(self, valor_transaccion_subtotal, mensaje='El valor de la transaccion debe ser positivo'):
        super().__init__(mensaje)
        self.valor_transaccion_subtotal = valor_transaccion_subtotal

    def es_valido(self) -> bool:
        return self.valor_transaccion_subtotal > 0