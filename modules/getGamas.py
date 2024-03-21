import json
import requests

def getAllGama():
    # http://154.38.171.54:5004/gama
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllId(id):
    peticion = requests.get(f'http://154.38.171.54:5004/gama/{id}')
    if peticion.ok:
        return [peticion.json()]
    else:
        return []

def getAllNombre():
     GamaNombre = []
     for val in getAllGama():
         GamaNombre.append(val.get('gama'))
     return GamaNombre

def getAllProductoGama(gama):
    for val in getAllGama():
        if val.get('gama') == gama:
            return [val]
    