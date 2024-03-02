from propiedadesDA.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesDA.seedwork.aplicacion.queries import ejecutar_query as query
# from propiedadesDA.modulos.analisis.infraestructura.repositorios import RepositorioPropiedadesAnalisisSQL
from dataclasses import dataclass
# from .base import PropiedadAnalisisQueryBaseHandler
from propiedadesDA.modulos.catastro.aplicacion.mapeadores import MapeadorCatastroDTOJson

@dataclass
class ObtenerCatastro(Query):
    id: str

class ObtenerCatastroHandler(PropiedadAnalisisQueryBaseHandler):

    def handle(self, query: ObtenerCatastro) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedadesAnalisisSQL.__class__)
        catastro =  self.fabrica_propiedad_analisis.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedadAnalisis())
        return QueryResultado(resultado=catastro)

@query.register(ObtenerCatastro)
def ejecutar_query_obtener_propiedad(query: ObtenerCatastro):
    handler = ObtenerCatastroHandler()
    return handler.handle(query)
