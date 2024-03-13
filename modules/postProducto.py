import json
import requests


def postProducto(producto):
    #json-server storage/producto.json -b 5502
    peticion = requests.post("http://172.16.100.116:5502", data=json.dumps(producto))
    res = peticion.json
    return res

