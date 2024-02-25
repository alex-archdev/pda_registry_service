from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class PropiedadRegistrada(EventoDominio):
    propiedad_id: str = None
    estado: str = None
