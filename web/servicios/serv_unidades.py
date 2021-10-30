import requests

from web.servicios import rest_api

def obtener_unidades():
    respuesta = requests.get(f'{rest_api.API_URL}/unidad')
    return respuesta.json()