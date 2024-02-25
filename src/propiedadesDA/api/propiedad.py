from flask import Blueprint, jsonify, request, Response
from propiedadesDA.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedadesDA.modulos.propiedad.aplicacion.comandos.registrar_propiedad import RegistrarPropiedad
from propiedadesDA.seedwork.aplicacion.comandos import ejecutar_comando

pb = Blueprint('propiedad', __name__)

@pb.route('/propiedad/health', methods = ['GET'])
def health():
    return jsonify({'result': 'OK'})

@pb.route('/propiedad', methods = ['POST'])
def registrar():
    propiedad_dict = request.json
    map_propiedad = MapeadorPropiedadDTOJson()
    propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
    comando = RegistrarPropiedad(
        propiedad_dto.nombre,
        propiedad_dto.coordenadas,
        propiedad_dto.direccion,
        propiedad_dto.fecha_actualizacion,
        propiedad_dto.fecha_creacion
        )

    ejecutar_comando(comando)
    
    return Response('{}', status=202, mimetype='application/json')
