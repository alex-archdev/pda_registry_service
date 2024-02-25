from dataclasses import dataclass, field
from propiedadesDA.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    coordenadas: str = field(default_factory=str)