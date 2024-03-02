# from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.seedwork.dominio.entidades import AgregacionRaiz
# from propiedadesDA.modulos.analisis.dominio.eventos import PropiedadAnalisisRegistrada

@dataclass
class Catastro(AgregacionRaiz):
    numero_catastral: str = field(default=str)
    propiedad_id: str = field(default=str)
    estrato: str = field(default=str)
    pisos: str = field(default=str)
    
    # def registrar_propiedad(self, propiedad: PropiedadAnalisis):
    #     self.agregar_evento(PropiedadAnalisisRegistrada(id=self.id))
