from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class PropiedadAnalisisRegistrada(EventoDominio):
    propiedad_id: str = None
