import json
import requests
from tabulate import tabulate
import getProducto as gP

def updateProducto(codigo):
    while True:
        if(codigo != None):
            producto = gP.getProductoCodigo(codigo)
            if (producto):
                print(tabulate(producto, headers='keys', tablefmt='fanxy grid'))
                opc = int(input("""

                        ¿Este es el producto que desea actualizar?
                                        1. Si
                                        2. No
                    
                """))
                if (opc):
                    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]['nombre'] = input('Ingrese el nuevo nombre del producto => ')
                    peticion = requests.put(f"http://154.38.171.54:5008/productos/{producto[0].get('id')}", headers=headers, data=json.dumps(producto))
                    data = peticion.json()
                    return [data]
                
                else:
                    codigo = None
            else:
                print(f'El producto {codigo} no existe')
                codigo = None
        else:
            codigo = input('Ingrese el código del producto que dese actualizar => ')