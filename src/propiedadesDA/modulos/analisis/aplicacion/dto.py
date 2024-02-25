from dataclasses import dataclass, field
from propiedadesDA.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadAnalisisDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    estado: str = field(default_factory=str)