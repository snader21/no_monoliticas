from src.modulos.propiedad.dominio.fabricas import FabricaPropiedad
from src.modulos.propiedad.infraestructura.fabricas import FabricaRepositorio
from src.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedades
from src.seedwork.aplicacion.servicios import Servicio


class ServicioPropiedad(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transaccion: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def actualizar_compania_duena(self, propiedad_id: str, nueva_compania: str):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedades.__class__)
        propiedad = repositorio.obtener_por_id(
            propiedad_id)
        propiedad.actualizar_compania_duena(nueva_compania)
        repositorio.actualizar(propiedad)

    def actualizar_datos_geograficos(self, propiedad_id: str, latitud: str, longitud: str):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedades.__class__)
        propiedad = repositorio.obtener_por_id(
            propiedad_id)
        propiedad.actualizar_datos_geograficos(latitud, longitud)
        repositorio.actualizar(propiedad)
