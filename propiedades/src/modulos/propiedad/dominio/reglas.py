from src.seedwork.dominio.reglas import ReglaNegocio


class PaisesValidos(ReglaNegocio):

    def __init__(self, pais, mensaje='El pais tiene que ser Colombia, Ecuador o Perú'):
        super().__init__(mensaje)
        self.pais = pais

    def es_valido(self) -> bool:
        paises_validos = ['Colombia', 'Ecuador', 'Peru']
        return self.pais in paises_validos


class TamanoPositivo(ReglaNegocio):

    def __init__(self, tamano, mensaje='El tamano debe ser positivo'):
        super().__init__(mensaje)
        self.tamano = tamano

    def es_valido(self) -> bool:
        return self.tamano > 0


class EsRequerido(ReglaNegocio):

    def __init__(self, campo, mensaje='El campo es requerido'):
        super().__init__(mensaje)
        self.campo = campo

    def es_valido(self) -> bool:
        return self.campo is not None and self.campo != ''
