from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.modulos.analisis.dominio.entidades import PropiedadAnalisis
from .dto import PropiedadAnalisis as PropiedadAnalisisDTO

class MapeadorPropiedadAnalisis(Mapeador):

    def obtener_tipo(self) -> type:
        return PropiedadAnalisis.__class__

    def entidad_a_dto(self, entidad: PropiedadAnalisis) -> PropiedadAnalisisDTO:
        propiedad_dto = PropiedadAnalisisDTO(
            entidad.propiedad_id,
            entidad.estado,
            entidad.fecha_creacion,
            entidad.fecha_actualizacion
        )

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadAnalisisDTO) -> PropiedadAnalisis:
        propiedad = PropiedadAnalisis(
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            estado=dto.estado,
            propiedad_id=dto.propiedad_id,
        )
        
        return propiedad