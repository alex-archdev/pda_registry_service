from propiedadesDA.seedwork.aplicacion.queries import QueryHandler
from propiedadesDA.modulos.analisis.infraestructura.fabricas import FabricaRepositorio
from propiedadesDA.modulos.analisis.dominio.fabricas import FabricaPropiedadAnalisis

class PropiedadAnalisisQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedad_analisis: FabricaPropiedadAnalisis = FabricaPropiedadAnalisis()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedad_analisis(self):
        return self._fabrica_propiedad_analisis    