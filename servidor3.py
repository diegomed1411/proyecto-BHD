from flask import Flask, request, jsonify
from servicios.autenticacion import autenticacion
from servicios.reclamos import reclamos
from flask import render_template

app = Flask(__name__)

@app.route('/')
def get_index():
    titulo_proyecto = 'BHD SOLUTIONS'
    return render_template('login.html', titulo=titulo_proyecto)

@app.route('/usuarioResidente',methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'idUsuario' not in datos_usuario:
        return 'El identificador de usuario es requerido', 412
    if 'nombre' not in datos_usuario:
        return 'El nombre es requerido', 412
    if 'apellido' not in datos_usuario:
        return 'El apellido es requerido', 412
    if 'email' not in datos_usuario:
        return 'El email es requerido', 412
    if 'tipoDocumento' not in datos_usuario:
        return 'El tipo de documento requerido', 412
    if 'numeroDeDocumento' not in datos_usuario:
        return 'El numero de documento es requerido', 412
    if 'telefono' not in datos_usuario:
        return 'El telefono es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    if 'idUnidad' not in datos_usuario:
        return 'La Unidad es requerida', 412
    if 'idInmueble' not in datos_usuario:
        return 'El inmueble es requerido', 412
    try:
        autenticacion.crear_usuario(datos_usuario['idUsuario'], datos_usuario['nombre'], datos_usuario['apellido'], datos_usuario['email'], datos_usuario['tipoDocumento'], datos_usuario['numeroDeDocumento'], datos_usuario['telefono'], datos_usuario['clave'], datos_usuario['idUnidad'], datos_usuario['idInmueble'])
    except Exception:
        return 'El usuario ya existe', 412
    return 'OK', 200


@app.route('/usuarioResidente/<id_usuario>', methods=['PUT'])
def modificar_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'email' not in datos_usuario or datos_usuario['email'] == '':
        return 'El email de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.modificar_usuario(id_usuario, datos_usuario)
    return 'OK', 200


@app.route('/usuarioResidente', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.obtener_usuarios())

@app.route('/usuarioResidente/<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    usuario = autenticacion.obtener_usuario(id_usuario)
    return jsonify(usuario)





@app.route('/usuarioResidente/<id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    autenticacion.borrar_usuario(id_usuario)
    return "Borrado", 200


@app.route('/reclamo', methods=['POST'])
def crear_reclamo():
    datos_reclamo = request.get_json()
    if 'idReclamo' not in datos_reclamo:
        return 'id de reclamo requerido', 412
    if 'descripcion' not in datos_reclamo:
        return 'descripcion requerida', 412
    if 'idInmueble' not in datos_reclamo:
        return 'se debe indicar el inmueble', 412
    if 'idUnidad' not in datos_reclamo:
        return 'se debe indicar la unidad', 412
    if 'idUsuario' not in datos_reclamo:
        return 'se debe especificar el usuario', 412
    if 'idServicio' not in datos_reclamo:
        return 'se debe indicar el identificador de servicio', 412
    #if 'fecha' not in datos_reclamo:
    #    return 'se debe indicar la fecha', 412
    #if 'estado' not in datos_reclamo:
    #    return 'se debe indicar el estado', 412
    #try:
    reclamos.crear_reclamo(datos_reclamo['idReclamo'], datos_reclamo['descripcion'], datos_reclamo['idInmueble'], datos_reclamo['idUnidad'], datos_reclamo['idUsuario'], datos_reclamo['idServicio'])
    #except Exception:
    #  return "el reclamo ya existe", 412
    return 'OK', 200

"""
@app.route('/reclamo/<id_reclamo>', methods=['PUT'])
def modificar_reclamo(idReclamo):
    datos_reclamo = request.get_json()
    if 'id_reclamo' not in datos_reclamo or datos_reclamo['idReclamo'] == '':
        return 'El id de reclamo es requerido', 412
    autenticacion.modificar_reclamo(idReclamo, datos_reclamo)
    return 'OK', 200
"""

@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'email' not in datos_usuario:
        return 'El email es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        id_sesion = autenticacion.login(datos_usuario['email'], datos_usuario['clave'])
        return jsonify({"id_sesion": id_sesion})
    except Exception:
        return 'USUARIO NO ENCONTRADO', 404




if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
