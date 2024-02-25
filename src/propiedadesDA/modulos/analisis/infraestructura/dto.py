from propiedadesDA.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class PropiedadAnalisis(Base):
    __tablename__ = "propiedades_analisis"
    id = Column(Integer, primary_key=True, autoincrement=True)
    propiedad_id = Column(String)
    estado = Column(String)
    fecha_creacion = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    def __init__(self, propiedad_id, estado, fecha_creacion, fecha_actualizacion):
        self.propiedad_id = propiedad_id
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion