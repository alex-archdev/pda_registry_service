from propiedadesDA.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class Propiedad(Base):
    __tablename__ = "propiedades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    _id = Column(String)
    nombre = Column(String)
    direccion = Column(String)
    coordenadas = Column(String)
    fecha_creacion = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    def __init__(self, _id, nombre, direccion, coordenadas, fecha_creacion, fecha_actualizacion):
        self._id = _id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion