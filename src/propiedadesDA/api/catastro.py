from flask import Blueprint, Response
from propiedadesDA.modulos.catastro.aplicacion.queries.obtener_catastro import ObtenerCatastro
from propiedadesDA.modulos.catastro.aplicacion.mapeadores import MapeadorCatastroDTOJson
from propiedadesDA.seedwork.aplicacion.queries import ejecutar_query

ca = Blueprint('catastro', __name__)

@ca.route('/catastro/health', methods = ['GET'])
def health():
    return Response({'result': 'OK'})

@ca.route('/catastro/propiedad/<id>', methods = ['GET'])
def obtener_catastro(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCatastro(id))
        map_catastro = MapeadorCatastroDTOJson()
        return map_catastro.dto_a_externo(query_resultado.resultado)
    else:
        return Response({'message': 'GET'})
