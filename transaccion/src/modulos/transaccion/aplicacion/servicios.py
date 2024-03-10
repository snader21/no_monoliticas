from src.modulos.transaccion.dominio.fabricas import FabricaTransaccion
from src.modulos.transaccion.infraestructura.fabricas import FabricaRepositorio
from src.modulos.transaccion.infraestructura.mapeadores import MapeadorTransaccion
from src.modulos.transaccion.infraestructura.repositorios import RepositorioTransacciones
from src.seedwork.aplicacion.servicios import Servicio
from src.modulos.transaccion.dominio.entidades import Transaccion
from pydispatch import dispatcher


class ServicioTransaccion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transaccion: FabricaTransaccion = FabricaTransaccion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_vuelos(self):
        return self._fabrica_transaccion

    @property
    def fabrica_transacciones(self):
        return self._fabrica_transaccion

    def crear_transaccion(self, descripcion: str, tipo: str, compania_origen: str, compania_destino: str, pais_transaccion_origen: str, valor_transaccion_subtotal: int, id_propiedad: str, id_correlacion: str):
        try:
            transaccion = Transaccion(descripcion=descripcion, tipo=tipo, compania_origen=compania_origen, compania_destino=compania_destino,
                                      pais_transaccion_origen=pais_transaccion_origen, valor_transaccion_subtotal=valor_transaccion_subtotal, id_propiedad=id_propiedad)
            repositorio = self.fabrica_repositorio.crear_objeto(
                RepositorioTransacciones.__class__)
            id_transaccion = repositorio.agregar(transaccion)
            dispatcher.send(signal='TransaccionCreada', id_transaccion=str(id_transaccion), id_correlacion=id_correlacion)
        except Exception as e:
            print('ERROR AL CREAR LA TRANSACCION', e)
            dispatcher.send(signal='ErrorCreandoTransaccion',
                            evento=id_propiedad)

    def borrar_transaccion(self, id_transaccion: str):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        repositorio.eliminar(id_transaccion)

    def obtener_transacciones(self):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        return repositorio.obtener_todos()

    def actualizar_impuestos(self, comania_origen_id: str, nuevo_pais: str):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioTransacciones.__class__)
        transacciones = repositorio.obtener_por_compania_origen_id(
            comania_origen_id)
        for transaccion in transacciones:
            transaccion.actualizar_impuesto(nuevo_pais)
            repositorio.actualizar(transaccion)
