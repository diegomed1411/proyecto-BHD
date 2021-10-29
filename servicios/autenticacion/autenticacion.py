from datos.modelos import reclamo as modelo_reclamo
#from datos.modelos import inmueble as modelo_inmueble
#from datos.modelos import unidades as modelo_unidades
from datos.modelos import usuarioResidente as modelo_usuario
from datetime import datetime


def _existe_usuario(email, clave):
    usuarios = modelo_usuario.obtener_usuarios_por_email_clave(email, clave)
    return not len(usuarios) == 0


def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.crear_sesion(id_usuario, dt_string)

# ------------------  listar todos los usuarios ---------------
def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()

# ------------------  listar un usuario segun id ---------------
def obtener_usuario(email):
    usuarios = modelo_usuario.obtener_usuario(email)
    if len(usuarios) == 0:
        raise Exception("El usuario no existe")
    return usuarios[0]



def crear_usuario( nombre, apellido, email, tipoDocumento, numeroDeDocumento, telefono, clave, idUnidad, idInmueble):
    modelo_usuario.crear_usuario( nombre, apellido, email, tipoDocumento, numeroDeDocumento, telefono, clave, idUnidad, idInmueble)


def modificar_usuario(id_usuario, datos_usuario):
    modelo_usuario.modificar_usuario(id_usuario, datos_usuario)


def borrar_usuario(id_usuario):
    modelo_usuario.borrar_usuario(id_usuario)


def login(email, clave):
    if _existe_usuario(email, clave):
        usuario = modelo_usuario.obtener_usuarios_por_email_clave(email, clave)[0]
        return _crear_sesion(usuario['id'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")


def validar_sesion(id_sesion):
    sesiones = modelo_usuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 120:
        # Sesion expirada
        return False
    else:
        return True



