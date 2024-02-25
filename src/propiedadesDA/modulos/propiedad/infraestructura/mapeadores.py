from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.modulos.propiedad.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(
            entidad.id,
            entidad.nombre,
            entidad.direccion,
            entidad.coordenadas,
            entidad.fecha_creacion,
            entidad.fecha_actualizacion
        )

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(
            dto.nombre,
            dto.direccion,
            dto.coordenadas,
            dto.fecha_creacion,
            dto.fecha_actualizacion,
        )
        
        return propiedad