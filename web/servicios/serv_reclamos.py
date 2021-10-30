import requests
from datetime import datetime
from web.servicios import rest_api

def obtener_reclamos():
    respuesta = requests.get(f'{rest_api.API_URL}/reclamo')
    return respuesta.json()



def crear_reclamo (id_reclamo, descripcion):
    body = {
        "id_reclamo": id_reclamo,
        "descripcion": descripcion,
        "id_inmueble": "EDA123MVDUY",
        "tipoDocumento": tipoDocumento,
        "numeroDeDocumento": numeroDeDocumento,
        "telefono": telefono,
        "clave": clave,
        "idUnidad": idUnidad,
        "idInmueble": idInmueble
    }
    respuesta = requests.post(f'{rest_api.API_URL}/usuarioResidente', json=body)
    return respuesta.status_code == 200