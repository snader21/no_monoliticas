from limpieza.src.dominio.entidades import Propiedad
from src.modulos.propiedad.dominio.fabricas import FabricaPropiedad
from src.modulos.propiedad.infraestructura.fabricas import FabricaRepositorio
from src.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedades
from src.seedwork.aplicacion.servicios import Servicio
from pydispatch import dispatcher

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
        print("PROPIEDAD!!!!!")
        print(propiedad)
        propiedad.actualizar_datos_geograficos(latitud, longitud)
        repositorio.actualizar(propiedad)

    def crear_propiedad(self, compania_duena: str, compania_arrendataria: str, direccion: str, tamano: int, pais_ubicacion: str, id_correlacion: str):
        try: 
            propiedad = Propiedad(
                compania_duena=compania_duena, 
                compania_arrendataria=compania_arrendataria, 
                direccion=direccion, 
                tamano=tamano, 
                pais_ubicacion=pais_ubicacion
            )
            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
            id_propiedad = repositorio.agregar(propiedad)
            dispatcher.send(signal='PropiedadCreadaIntegracion', evento={'id': id_propiedad, 'direccion': propiedad.direccion})
        except Exception as e:
            print(e)
            dispatcher.send(signal='ErrorCreandopropiedad', evento=id_correlacion)

    
    def borrar_propiedad(self, id_propiedad: str):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.eliminar(id_propiedad)
