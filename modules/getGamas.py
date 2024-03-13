import json
import requests

def getAllGama():
    #json-server storage/gama_producto.json -b 5503
    peticion = requests.get("")
    data = peticion.json()
    return data

def getAllNombre():
     GamaNombre = []
     for val in getAllGama():
         GamaNombre.append({
             "nombre": val.get("nombre"),
         })