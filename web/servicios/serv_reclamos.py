import requests
from web.servicios import rest_api

def obtener_reclamos():
    respuesta = requests.get(f'{rest_api.API_URL}/reclamo')
    return respuesta.json()



def crear_reclamo ( descripcion, id_servicio ,id_usuario):
    body = {
        "descripcion": descripcion,
        "idInmueble": "EDA123MVDUY",
        "idUnidad": "EDA123A103",
        "idUsuario": id_usuario,
        "idServicio": id_servicio
    }
    respuesta = requests.post(f'{rest_api.API_URL}/reclamo', json=body)
    return respuesta.status_code == 200

def borrar_reclamo (id):
    respuesta = requests.delete(f'{rest_api.API_URL}/relamo/{id}')
    return respuesta.status_code == 200