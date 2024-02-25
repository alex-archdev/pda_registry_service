from propiedadesDA.seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from propiedadesDA.modulos.propiedad.aplicacion.dto import PropiedadDTO
from propiedadesDA.modulos.propiedad.dominio.entidades import Propiedad

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO
        propiedad_dto.coordenadas = externo.get('coordenadas')
        propiedad_dto.direccion = externo.get('direccion')
        propiedad_dto.fecha_actualizacion = externo.get('fecha_creacion')
        propiedad_dto.fecha_creacion = externo.get('fecha_creacion')
        propiedad_dto.nombre = externo.get('nombre')
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__
    
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.coordenadas = dto.coordenadas
        propiedad.direccion = dto.direccion
        propiedad.fecha_actualizacion = dto.fecha_actualizacion
        propiedad.fecha_creacion = dto.fecha_creacion
        propiedad.nombre = dto.nombre

        return propiedad