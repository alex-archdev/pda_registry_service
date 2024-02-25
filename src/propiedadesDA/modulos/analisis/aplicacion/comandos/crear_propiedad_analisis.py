from dataclasses import dataclass
from propiedadesDA.seedwork.aplicacion.comandos import Comando
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando as comando
from propiedadesDA.modulos.analisis.aplicacion.dto import PropiedadAnalisisDTO
from propiedadesDA.modulos.analisis.dominio.entidades import PropiedadAnalisis
from propiedadesDA.modulos.analisis.aplicacion.mapeadores import MapeadorPropiedadAnalisis
from propiedadesDA.modulos.analisis.infraestructura.repositorios import RepositorioPropiedadesAnalisisSQL
from propiedadesDA.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .base import RegistrarPropiedadAnalisisBaseHandler

@dataclass
class RegistrarPropiedadAnalisis(Comando):
    estado: str
    fecha_actualizacion: str
    fecha_creacion: str
    propiedad_id: str

class RegistrarPropiedadAnalisisHandler(RegistrarPropiedadAnalisisBaseHandler):
    
    def handle(self, comando: RegistrarPropiedadAnalisis):
        propiedad_dto = PropiedadAnalisisDTO(
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            propiedad_id=comando.propiedad_id,
            estado=comando.estado
        )

        propiedad: PropiedadAnalisis = self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedadAnalisis())
        propiedad.registrar_propiedad(propiedad)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedadesAnalisisSQL.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()


@comando.register(RegistrarPropiedadAnalisis)
def ejecutar_comando_crear_reserva(comando: RegistrarPropiedadAnalisis):
    handler = RegistrarPropiedadAnalisisHandler()
    handler.handle(comando)