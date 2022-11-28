from flask import Flask, jsonify, request
import db_controller
from db import create_tables

app = Flask(__name__)

# Obtiene una lista de todos los abonados
@app.route("/abonados", methods=["GET"])
def get_abonados():
    abonados = db_controller.get_abonados()
    return jsonify(abonados)

# Obtiene una lista de todos los servicios
@app.route("/servicios", methods=["GET"])
def get_servicios():
    servicios = db_controller.get_servicios()
    return jsonify(servicios)

# Crea un nuevo abonado
@app.route("/abonado", methods=["POST"])
def insert_abonado():
    abonado_details = request.get_json()
    nombre = abonado_details["nombre"]
    servicio_id = abonado_details["servicio_id"]
    result = db_controller.insert_abonado(nombre, servicio_id)
    return jsonify(result)

# Crea un nuevo servicio
@app.route("/servicio", methods=["POST"])
def insert_servicio():
    servicio_details = request.get_json()
    tipo = servicio_details["tipo"]
    precio = servicio_details["precio"]
    result = db_controller.insert_servicio(tipo, precio)
    return jsonify(result)

# Actualiza abonado
@app.route("/abonados", methods=["PUT"])
def update_abonado():
    abonados_details = request.get_json()
    id = abonados_details["id"]
    nombre = abonados_details["nombre"]
    servicio_id = abonados_details["servicio_id"]
    result = db_controller.update_abonado(id, nombre, servicio_id)
    return jsonify(result)

# Actualiza servicio
@app.route("/servicios", methods=["PUT"])
def update_servicio():
    servicios_details = request.get_json()
    id = servicios_details["id"]
    tipo = servicios_details["tipo"]
    precio = servicios_details["precio"]
    result = db_controller.update_servicio(id, tipo, precio)
    return jsonify(result)

# Elimina abonado particular (el que coincide con el ID)
@app.route("/abonado/<id>", methods=["DELETE"])
def delete_abonado(id):
    result = db_controller.delete_abonado(id)
    return jsonify(result)

# Elimina servicio particular (el que coincide con el ID)
@app.route("/servicio/<id>", methods=["DELETE"])
def delete_servicio(id):
    result = db_controller.delete_servicio(id)
    return jsonify(result)

# Obtiene abonado particular (el que coincide con el ID)
@app.route("/abonado/<id>", methods=["GET"])
def get_abonado_by_id(id):
    abonado = db_controller.get_abonado_by_id(id)
    return jsonify(abonado)

# Obtiene servicio particular (el que coincide con el ID)
@app.route("/servicio/<id>", methods=["GET"])
def get_servicio_by_id(id):
    servicio = db_controller.get_servicio_by_id(id)
    return jsonify(servicio)

if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)