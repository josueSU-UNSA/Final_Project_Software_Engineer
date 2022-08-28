from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.ponente import PonenteModel
from backend.infrastructure.ponente_repository import PonenteRepository

ponente_blueprint = Blueprint('ponente_blueprint', __name__)

repo = PonenteRepository()

@ponente_blueprint.route('/ponente/create', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def create_asistente():
    content = repo.create(int(request.json['id']), request.json['nombre'], request.json['apellido'], request.json['correo'])    
    return jsonify(content)

@ponente_blueprint.route('/ponente/get', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def get_asistente():
    content = repo.get(int(request.json['id']))    
    return jsonify(content)

@ponente_blueprint.route('/ponente/create', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def get_all_asistente():
    content = repo.get_all() 
    return jsonify(content)

@ponente_blueprint.route('/ponente/create', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def delete_asistente():
    content = repo.delete(int(request.json['id']))    
    return jsonify(content)