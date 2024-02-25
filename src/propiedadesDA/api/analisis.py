from flask import Blueprint, Response
from propiedadesDA.modulos.analisis.aplicacion.queries.obtener_propiedad import ObtenerPropiedadAnalisis
from propiedadesDA.modulos.analisis.aplicacion.mapeadores import MapeadorPropiedadAnalisisDTOJson
from propiedadesDA.seedwork.aplicacion.queries import ejecutar_query

ab = Blueprint('analisis', __name__)

@ab.route('/analisis/health', methods = ['GET'])
def health():
    return Response({'result': 'OK'})

@ab.route('/analisis/propiedad/<id>', methods = ['GET'])
def dar_propiedad(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedadAnalisis(id))
        map_propiedad = MapeadorPropiedadAnalisisDTOJson()
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return Response({'message': 'GET'})
