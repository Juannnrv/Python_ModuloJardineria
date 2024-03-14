import json
import requests

def getAllGama():
    #json-server storage/gama_producto.json -b 5503
    peticion = requests.get("http://172.16.100.116:5503")
    data = peticion.json()
    return data

def getAllNombre():
     GamaNombre = []
     for val in getAllGama():
         GamaNombre.append(val.get('gama'))
     return GamaNombre