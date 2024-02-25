from dataclasses import dataclass
from propiedadesDA.seedwork.aplicacion.comandos import Comando
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando as comando
from propiedadesDA.modulos.propiedad.aplicacion.dto import PropiedadDTO
from propiedadesDA.modulos.propiedad.dominio.entidades import Propiedad
from propiedadesDA.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedadesDA.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedadesSQL
from propiedadesDA.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .base import RegistrarPropiedadBaseHandler

@dataclass
class RegistrarPropiedad(Comando):
    nombre: str
    coordenadas: str
    direccion: str
    fecha_actualizacion: str
    fecha_creacion: str

class RegistrarPropiedadHandler(RegistrarPropiedadBaseHandler):
    
    def handle(self, comando: RegistrarPropiedad):
        propiedad_dto = PropiedadDTO(
            nombre=comando.nombre,
            coordenadas=comando.coordenadas,
            direccion=comando.direccion,
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion
        )
        try:
            propiedad: Propiedad = self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedadDTOJson())
            propiedad.registrar_propiedad(propiedad)

            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedadesSQL.__class__)

            UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
            UnidadTrabajoPuerto.savepoint()
            UnidadTrabajoPuerto.commit()
        except Exception as e:
            UnidadTrabajoPuerto.rollback()


@comando.register(RegistrarPropiedad)
def ejecutar_comando_crear_reserva(comando: RegistrarPropiedad):
    handler = RegistrarPropiedadHandler()
    handler.handle(comando)