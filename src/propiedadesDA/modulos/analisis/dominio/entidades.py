from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.seedwork.dominio.entidades import AgregacionRaiz
import propiedadesDA.modulos.analisis.dominio.objeto_valor as ov
from propiedadesDA.modulos.analisis.dominio.eventos import PropiedadAnalisisRegistrada

@dataclass
class PropiedadAnalisis(AgregacionRaiz):
    estado: ov.EstadoPropiedad = field(default=str)
    propiedad_id: str = field(default=str)
    fecha_creacion: str = field(default=str)
    fecha_actualizacion: str = field(default=str)
    
    def registrar_propiedad(self, propiedad: PropiedadAnalisis):

        self.agregar_evento(PropiedadAnalisisRegistrada(id=self.id))
