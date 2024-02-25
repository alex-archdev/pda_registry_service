from propiedadesDA.seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from propiedadesDA.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesDA.modulos.analisis.aplicacion.dto import PropiedadAnalisisDTO
from propiedadesDA.modulos.analisis.dominio.entidades import PropiedadAnalisis

class MapeadorPropiedadAnalisisDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadAnalisisDTO:
        propiedad_dto = PropiedadAnalisisDTO
        propiedad_dto.fecha_actualizacion = externo.get('fecha_creacion')
        propiedad_dto.fecha_creacion = externo.get('fecha_actualizacion')
        propiedad_dto.estado = externo.get('estado')
        propiedad_dto.propiedad_id = externo.get('propiedad_id')
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadAnalisisDTO) -> dict:
        return dto.__dict__
    
    def obtener_tipo(self) -> type:
        return PropiedadAnalisis.__class__


class MapeadorPropiedadAnalisis(RepMap):
    def dto_a_entidad(self, dto: PropiedadAnalisisDTO) -> PropiedadAnalisis:
        entidad = PropiedadAnalisis()
        entidad.estado = dto.estado
        entidad.fecha_actualizacion = dto.fecha_actualizacion
        entidad.fecha_creacion = dto.fecha_creacion
        entidad.propiedad_id = dto.propiedad_id

        return entidad
    
    def entidad_a_dto(self, entidad: PropiedadAnalisis) -> PropiedadAnalisisDTO:
        dto = PropiedadAnalisisDTO(
            entidad.fecha_creacion,
            entidad.fecha_actualizacion,
            entidad.propiedad_id,
            entidad.estado
        )
        return dto
    
    def obtener_tipo(self) -> type:
        return PropiedadAnalisis.__class__