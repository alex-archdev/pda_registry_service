from dataclasses import dataclass, field
from propiedadesDA.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CatastroDTO(DTO):
    numero_catastral: str = field(default_factory=str)
    estrato: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    pisos: str = field(default_factory=str)