import requests
from web.servicios import rest_api

def obtener_servicios():
    respuesta = requests.get(f'{rest_api.API_URL}/servicios')
    return respuesta.json()