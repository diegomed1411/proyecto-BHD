from datos.modelos import usuarioResidente as modelo_usuario
from datos.modelos import reclamo as modelo_reclamo
#from datos.modelos import inmueble as modelo_inmueble
#from datos.modelos import unidades as modelo_unidades
from datos.modelos import usuarioResidente as modelo_usuario

def crear_usuario(idUsuario, nombre, apellido, email, tipoDocumento, numeroDeDocumento, telefono, clave, idUnidad, idInmueble):
    modelo_usuario.crear_usuario(idUsuario, nombre, apellido, email, tipoDocumento, numeroDeDocumento, telefono, clave, idUnidad, idInmueble)

def modificar_usuario(id_usuario, datos_usuario):
    modelo_usuario.modificar_usuario(id_usuario, datos_usuario)

def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()

def borrar_usuario(id_usuario):
    modelo_usuario.borrar_usuario(id_usuario)

#def crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio):
    modelo_reclamo.crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio)

#def crear_inmueble(idInmueble, nombreInmueble, direccion, cantidadUnidades, servicios, identificadorCocheras, actas, unidadesActivas, listaAmenities):
    modelo_inmueble.crear_inmueble(idInmueble, nombreInmueble, direccion, cantidadUnidades, servicios, identificadorCocheras, actas, unidadesActivas, listaAmenities)

#def crear_unidades(idUnidad, numeroUnidad, usuariosUnidad, gastosUnidad, idInmueble):
    modelo_unidades.crear_unidades(idUnidad, numeroUnidad, usuariosUnidad, gastosUnidad, idInmueble)