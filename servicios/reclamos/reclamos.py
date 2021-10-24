from datos.modelos import reclamo as modelo_reclamo


def crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio):
    modelo_reclamo.crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio)


def modificar_reclamo(id_reclamo, datos_reclamo):
    modelo_reclamo.modificar_reclamo(id_reclamo, datos_reclamo)

def obtener_reclamos():
    return modelo_reclamo.obtener_reclamos()

def obtener_reclamo(id_reclamo):
    reclamos= modelo_reclamo.obtener_reclamo(id_reclamo)
    if len(reclamos) == 0:
        raise Exception("El reclamo no existe")
    return reclamos[0]

def borrar_reclamo(id_reclamo):
    modelo_reclamo.borrar_reclamo(id_reclamo)




