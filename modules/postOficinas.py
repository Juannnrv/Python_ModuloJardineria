import json
import requests
import os
from tabulate import tabulate


def postOficina():
    # json-server storage/oficina.json -b 5007
    oficina = {
        "codigo_oficina": input('Ingresa el código de oficina => '),
        "ciudad": input('Ingresa la ciudad => '),
        "pais": input('Ingresa el país => '),
        "region": input('Ingresa la región  => '),
        "codigo_postal": input('Ingresa el código postal => '),
        "telefono": input('Ingresa el telefono => '),
        "linea_direccion1": input('Ingresa la direccion 1  => '),
        "linea_direccion2": input('Ingresa la direccion 2  => ')
    }

    headers = {'Content-Type': 'application/json', 'charser': 'UTF-8'}
    peticion = requests.post('http://172.16.100.116:5504', headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res ['Mensaje'] = 'Oficina Guardada'
    return [res]


def menu():
    while True:
        os.system('clear')
        print("""
               ---ADMINISTRADOR DATOS DE LAS OFICINAS---
          
                    1. Guardar un oficina nueva
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if opcion == 1:
                print(tabulate(postOficina(), headers='keys', tablefmt='fancy grid'))
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break