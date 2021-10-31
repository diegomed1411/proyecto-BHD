import requests
from web.servicios import rest_api

def obtener_reclamos():
    respuesta = requests.get(f'{rest_api.API_URL}/reclamo')
    return respuesta.json()

def obtener_reclamo_por_id (id):
    respuesta = requests.get(f'{rest_api.API_URL}/reclamo/{id}')
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
    respuesta = requests.delete(f'{rest_api.API_URL}/reclamo/{id}')
    return respuesta.status_code == 200

def modificar_reclamo (id):
    respuesta = requests.put(f'{rest_api.API_URL}/reclamo/{id}')
    return respuesta.status_code == 200
#{'descripcion': 'fdfsfs', 'estado': 'pendiente', 'fecha': '2021-10-30 15:35:34.014608', 'id': 13, 'id_inmueble': 'EDA123MVDUY', 'id_servicio': 'ELEC100', 'id_unidad': 'EDA123A103', 'id_usuario': 3}