from propiedadesDA.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from propiedadesDA.modulos.propiedad.dominio.fabricas import FabricaPropiedad
from propiedadesDA.modulos.propiedad.dominio.entidades import Propiedad
from uuid import UUID
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from propiedadesDA.conf.db import db_session


class RepositorioPropiedadesSQL(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> Propiedad:
        reserva_dto = db_session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedad.crear_objeto(reserva_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        ...

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedad.crear_objeto(propiedad, MapeadorPropiedad())
        db_session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        ...

    def eliminar(self, propiedad_id: UUID):
        ...