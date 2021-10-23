from datos.modelos import reclamo as modelo_reclamo


def crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio):
    modelo_reclamo.crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio)


def modificar_reclamo(id_reclamo, datos_reclamo):
    modelo_reclamo.modificar_reclamo(id_reclamo, datos_reclamo)


