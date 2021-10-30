import requests

from web.servicios import rest_api

def validar_credenciales(email, clave):
    body= {"email": email,
        "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200

def crear_usuario(nombre, apellido, email, tipoDocumento, numeroDeDocumento, telefono, clave, idUnidad, idInmueble):
    body={
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "tipoDocumento": tipoDocumento,
        "numeroDeDocumento": numeroDeDocumento,
        "telefono": telefono,
        "clave": clave,
        "idUnidad": idUnidad,
        "idInmueble": idInmueble
    }
    respuesta = requests.post(f'{rest_api.API_URL}/usuarioResidente', json=body)
    return respuesta.status_code==200

def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarioResidente')
    return respuesta.json()

