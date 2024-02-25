from propiedadesDA.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesDA.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadesDA.modulos.analisis.infraestructura.repositorios import RepositorioPropiedadesAnalisisSQL
from dataclasses import dataclass
from .base import PropiedadAnalisisQueryBaseHandler
from propiedadesDA.modulos.analisis.aplicacion.mapeadores import MapeadorPropiedadAnalisis

@dataclass
class ObtenerPropiedadAnalisis(Query):
    id: str

class ObtenerPropiedadAnalisisHandler(PropiedadAnalisisQueryBaseHandler):

    def handle(self, query: ObtenerPropiedadAnalisis) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedadesAnalisisSQL.__class__)
        propiedad_analisis =  self.fabrica_propiedad_analisis.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedadAnalisis())
        return QueryResultado(resultado=propiedad_analisis)

@query.register(ObtenerPropiedadAnalisis)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedadAnalisis):
    handler = ObtenerPropiedadAnalisisHandler()
    return handler.handle(query)
