from propiedadesDA.seedwork.aplicacion.comandos import ComandoHandler
from propiedadesDA.modulos.analisis.infraestructura.fabricas import FabricaRepositorio
from propiedadesDA.modulos.analisis.dominio.fabricas import FabricaPropiedadAnalisis

class RegistrarPropiedadAnalisisBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedad: FabricaPropiedadAnalisis = FabricaPropiedadAnalisis()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad