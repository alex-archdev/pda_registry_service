from propiedadesDA.modulos.analisis.dominio.repositorios import RepositorioPropiedadesAnalisis
from propiedadesDA.modulos.analisis.dominio.fabricas import FabricaPropiedadAnalisis
from propiedadesDA.modulos.analisis.dominio.entidades import PropiedadAnalisis
from uuid import UUID
from .dto import PropiedadAnalisis as PropiedadAnalisisDTO
from .mapeadores import MapeadorPropiedadAnalisis
from propiedadesDA.conf.db import db_session


class RepositorioPropiedadesAnalisisSQL(RepositorioPropiedadesAnalisis):

    def __init__(self):
        self._fabrica_propiedad_analisis: FabricaPropiedadAnalisis = FabricaPropiedadAnalisis()

    @property
    def fabrica_propiedad_analisis(self):
        return self._fabrica_propiedad_analisis

    def obtener_por_id(self, id: UUID) -> PropiedadAnalisis:
        reserva_dto = db_session.query(PropiedadAnalisisDTO).filter_by(propiedad_id=str(id)).one()
        return self.fabrica_propiedad_analisis.crear_objeto(reserva_dto, MapeadorPropiedadAnalisis())

    def obtener_todos(self) -> list[PropiedadAnalisis]:
        ...

    def agregar(self, propiedad: PropiedadAnalisis):
        propiedad_dto = self.fabrica_propiedad_analisis.crear_objeto(propiedad, MapeadorPropiedadAnalisis())
        db_session.add(propiedad_dto)

    def actualizar(self, propiedad: PropiedadAnalisis):
        ...

    def eliminar(self, propiedad_id: UUID):
        ...