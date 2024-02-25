from dataclasses import dataclass
from propiedadesDA.seedwork.dominio.fabricas import Fabrica
from propiedadesDA.seedwork.dominio.repositorios import Repositorio
from propiedadesDA.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioPropiedadesAnalisisSQL

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesAnalisisSQL()
        else:
            raise ExcepcionFabrica()