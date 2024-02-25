from src.recopilacion.modulos.transaccion.dominio.fabricas import FabricaTransaccion
from src.recopilacion.modulos.transaccion.infraestructura.fabricas import FabricaRepositorio
from src.recopilacion.modulos.transaccion.infraestructura.mapeadores import MapeadorTransaccion
from src.recopilacion.modulos.transaccion.infraestructura.repositorios import RepositorioTransacciones
from src.recopilacion.seedwork.aplicacion.servicios import Servicio


class ServicioReserva(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transaccion: FabricaTransaccion = FabricaTransaccion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_vuelos(self):
        return self._fabrica_transaccion

    def actualizar_impuestos(self, comania_origen_id: str, nuevo_pais: str):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        transacciones = repositorio.obtener_por_compania_origen_id(
            comania_origen_id)
        for transaccion in transacciones:
            transaccion.actualizar_impuesto(nuevo_pais)
            repositorio.actualizar(transaccion)
