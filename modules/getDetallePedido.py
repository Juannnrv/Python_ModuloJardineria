import json
import requests
import os

def getAllDetallePedido():
    peticion = requests.get('http://154.38.171.54:5001/cliente')
    data = peticion.json()
    return data

def getAllCodigos(codigo_pedido):
    for val in getAllDetallePedido():
      if (val.get('codigo_pedido') == codigo_pedido):
         return [val]


def getAllId(id):
    peticion = requests.get(f'http://154.38.171.54:5002/detalle_pedido/{id}')
    if peticion.ok:
        return [peticion.json()]
    else:
        return []
