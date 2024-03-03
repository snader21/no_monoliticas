from transaccion.src.modulos.transaccion.dominio.fabricas import FabricaTransaccion
from transaccion.src.modulos.transaccion.infraestructura.fabricas import FabricaRepositorio
from transaccion.src.modulos.transaccion.infraestructura.mapeadores import MapeadorTransaccion
from transaccion.src.modulos.transaccion.infraestructura.repositorios import RepositorioTransacciones
from transaccion.src.seedwork.aplicacion.servicios import Servicio


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
