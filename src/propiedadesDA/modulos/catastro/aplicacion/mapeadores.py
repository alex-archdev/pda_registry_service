from propiedadesDA.seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from propiedadesDA.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesDA.modulos.catastro.aplicacion.dto import CatastroDTO
from propiedadesDA.modulos.catastro.dominio.entidades import Catastro

class MapeadorCatastroDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> CatastroDTO:
        catastro_dto = CatastroDTO
        catastro_dto.numero_catastral = externo.get('numero_catastral')
        catastro_dto.estrato = externo.get('estrato')
        catastro_dto.pisos = externo.get('pisos')
        catastro_dto.propiedad_id = externo.get('propiedad_id')
        return catastro_dto
    
    def dto_a_externo(self, dto: CatastroDTO) -> dict:
        return dto.__dict__
    
    def obtener_tipo(self) -> type:
        return Catastro.__class__


class MapeadorCatastro(RepMap):
    def dto_a_entidad(self, dto: CatastroDTO) -> Catastro:
        entidad = Catastro()
        entidad.numero_catastral = dto.numero_catastral
        entidad.estrato = dto.estrato
        entidad.pisos = dto.pisos
        entidad.propiedad_id = dto.propiedad_id
        return entidad
    
    def entidad_a_dto(self, entidad: Catastro) -> CatastroDTO:
        dto = CatastroDTO(
            entidad.numero_catastral,
            entidad.estrato,
            entidad.propiedad_id,
            entidad.pisos
        )
        return dto
    
    def obtener_tipo(self) -> type:
        return Catastro.__class__