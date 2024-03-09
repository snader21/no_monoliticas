from src.modulos.compania.dominio.entidades import Compania
from src.modulos.compania.dominio.fabricas import FabricaCompania
from src.modulos.compania.infraestructura.fabricas import FabricaRepositorio
from src.modulos.compania.infraestructura.repositorios import RepositorioCompanias
from src.seedwork.aplicacion.servicios import Servicio
from pydispatch import dispatcher

class ServicioCompania(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_compania: FabricaCompania = FabricaCompania()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_compania(self):
        return self._fabrica_compania

    def crear_compania(self, tipoPersona: str, nombre: str, tipo: str, pais: str, identificacion: str, id_correlacion: str):
        try: 
            compania = Compania(tipoPersona= tipoPersona, 
                                nombre= nombre, 
                                tipo= tipo, 
                                pais= pais, 
                                identificacion= identificacion)
            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
            id_compania = repositorio.agregar(compania)
            dispatcher.send(signal='CompaniaCreada', evento=id_compania)
        except Exception as e:
            print(e)
            dispatcher.send(signal='ErrorCreandoCompania', evento=id_correlacion)

    
    def borrar_compania(self, id_compania: str):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        repositorio.eliminar(id_compania)
