from .entidades import PropiedadAnalisis
from .excepciones import TipoObjetoNoExisteEnDominioAnalisisExcepcion
from propiedadesDA.seedwork.dominio.repositorios import Mapeador
from propiedadesDA.seedwork.dominio.fabricas import Fabrica
from propiedadesDA.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPropiedadAnalisis(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad = mapeador.dto_a_entidad(obj)

            return propiedad

@dataclass
class FabricaPropiedadAnalisis(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == PropiedadAnalisis.__class__:
            fabrica_propiedad = _FabricaPropiedadAnalisis()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAnalisisExcepcion()