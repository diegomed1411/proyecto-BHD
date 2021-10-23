from datos.modelos import reclamo as modelo_reclamo


def crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio):
    modelo_reclamo.crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio)

"""
def modificar_reclamo(id_usuario, datos_usuario):
    modelo_usuario.modificar_usuario(id_usuario, datos_usuario)
"""

# hay que modificar tabla reclamos en base de datos