from propiedadesDA.modulos.analisis.aplicacion.mapeadores import MapeadorPropiedadAnalisisDTOJson
from propiedadesDA.modulos.analisis.aplicacion.comandos.crear_propiedad_analisis import RegistrarPropiedadAnalisis
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando
from datetime import datetime

class HandlePropiedadDominio():
    @staticmethod
    def handle_propiedad_registrada(evento):
        obj = {
            "fecha_creacion": datetime.now(),
            "fecha_actualizacion": datetime.now(),
            "propiedad_id": evento.propiedad_id,
            "estado": evento.estado
        }
        map_propiedad = MapeadorPropiedadAnalisisDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(obj)
        comando = RegistrarPropiedadAnalisis(
            propiedad_dto.estado,
            propiedad_dto.fecha_actualizacion,
            propiedad_dto.fecha_creacion,
            propiedad_dto.propiedad_id
        )

        ejecutar_comando(comando)