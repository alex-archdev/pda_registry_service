from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesDA.modulos.propiedad.dominio.eventos import PropiedadRegistrada
from propiedadesDA.seedwork.dominio.entidades import AgregacionRaiz
import propiedadesDA.modulos.propiedad.dominio.objeto_valor as ov

import uuid

@dataclass
class Propiedad(AgregacionRaiz):
    estado: ov.EstadoPropiedad = field(default=ov.EstadoPropiedad.EN_VALIDACION)
    nombre: str = field(default=str)
    coordenadas: str = field(default=str)
    direccion: str = field(default=str)

    def registrar_propiedad(self, propiedad: Propiedad):
        self.estado = propiedad.estado

        self.agregar_evento(PropiedadRegistrada(propiedad_id=self.id, estado=self.estado.name))

    # def aprobar_reserva(self):
    #     self.estado = ov.EstadoReserva.APROBADA

    #     self.agregar_evento(ReservaAprobada(self.id, self.fecha_actualizacion))

    # def cancelar_reserva(self):
    #     self.estado = ov.EstadoReserva.CANCELADA

    #     self.agregar_evento(ReservaCancelada(self.id, self.fecha_actualizacion))
    
    # def pagar_reserva(self):
    #     self.estado = ov.EstadoReserva.PAGADA

    #     self.agregar_evento(ReservaPagada(self.id, self.fecha_actualizacion))