from flask import Flask, request, jsonify
from servicios.autenticacion import autenticacion
from servicios.reclamos import reclamos

app = Flask(__name__)

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
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.modificar_usuario(id_usuario, datos_usuario)
    return 'OK', 200


@app.route('/usuarioResidente', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.obtener_usuarios())


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
    if 'fecha' not in datos_reclamo:
        return 'se debe indicar la fecha', 412
    #if 'estado' not in datos_reclamo:
    #    return 'se debe indicar el estado', 412
    try:
        reclamos.crear_reclamo(datos_reclamo['idReclamo'], datos_reclamo['descripcion'], datos_reclamo['idInmueble'], datos_reclamo['idUnidad'], datos_reclamo['idUsuario'], datos_reclamo['idServicio'], datos_reclamo['fecha'])
    except Exception:
      return "el usuario ya existe", 412
    return 'OK', 200


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

"""
@app.route('/reclamo/<id_reclamo>', methods=['PUT'])
def modificar_reclamo(idReclamo):
    datos_reclamo = request.get_json()
    if 'id_reclamo' not in datos_reclamo or datos_reclamo['idReclamo'] == '':
        return 'El id de reclamo es requerido', 412
    autenticacion.modificar_reclamo(idReclamo, datos_reclamo)
    return 'OK', 200
"""

"""
@app.route('/inmueble',methods=['POST'])
def crear_inmueble():
    datos_inmueble = request.get_json()
    if 'idInmueble' not in datos_inmueble:
        return 'idInmueble requerido', 412
    if 'nombreInmueble' not in datos_inmueble:
        return 'nombreInmueble requerido', 412
    if 'direccion' not in datos_inmueble:
        return 'direccion requerida', 412
    if 'cantidadUnidades' not in datos_inmueble:
        return 'cantidad de unidades requerida', 412
    if 'servicios' not in datos_inmueble:
        return 'servicios requerido', 412
    if 'identificadorCocheras' not in datos_inmueble:
        return 'identificador cocheras requerido', 412
    if 'unidadesActivas' not in datos_inmueble:
        return 'unidades activas requeridas', 412
    if 'listaAmenities' not in datos_inmueble:
        return 'lista amenities requerida', 412
    autenticacion.crear_inmueble(datos_inmueble['idInmueble'],datos_inmueble['nombreInmueble'],datos_inmueble['direccion'],datos_inmueble['cantidadUnidades'], datos_inmueble['servicios'], datos_inmueble['identificadorCocheras'], datos_inmueble['unidadesActivas'], datos_inmueble['listaAmenities'])
    return 'OK', 200


@app.route('/unidades', methods=['POST'])
def crear_unidades():
    datos_unidades = request.get_json()
    if 'idUnidad' not in datos_unidades:
        return 'Id unidad requerido', 412
    if 'numeroUnidad' not in datos_unidades:
        return 'numero de unidad requerido', 412
    if 'usuariosUnidad' not in datos_unidades:
        return 'usuario de la unidad requerido', 412
    if 'gastosUnidad' not in datos_unidades:
        return 'gastos requeridos', 412
    if 'idInmueble' not in datos_unidades:
        return 'id inmueble requerido', 412
    autenticacion.crear_unidades(datos_unidades['idUnidad'], datos_unidades['numeroUnidad'], datos_unidades['usuariosUnidad'], datos_unidades['gastosUnidad'], datos_unidades['idInmueble'])
    return 'OK', 200
"""

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
