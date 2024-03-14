import json
import requests
import os
from tabulate import tabulate


def postClientes():
    #json-server storage/cliente.json -b 5502

    cliente = {
        'codigo_producto': int(input('Ingrese el código del producto => ')),
        'nombre_cliente': input('Ingrese el nombre del cliente => '),
        'nombre_contacto': input('Ingrese el nombre del contacto => '),
        'apellido_contacto': input('Ingrese el apellido del contacto => '),
        'telefono': input('Ingrese el telefono => '),
        'fax': input('Ingrese el fax => '),
        'linea_direccion1': input('Ingrese la linea de direccion 1 => '),
        'linea_direccion2': input('Ingrese la linea de direccion 2 => '),
        'ciudad': input('Ingrese la ciudad => '),
        'region': input('Ingrese la region => '),
        'pais': input('Ingrese el pais => '),
        'codigo_postal': input('Ingrese el codigo postal => '),
        'codigo_empleado_rep_ventas': int(input('Ingresa el codigo del representante de ventas => ')),
        'limite_credito': int(input('Ingrese el limite crediticio => '))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'UTF -8'}
    peticion = requests.post('', headers=headers, data=json.dumps(cliente)) 
    res = peticion.json()
    res ['Mensaje'] = 'Cliente Guardado'
    return [res]

def menu():
    while True:
     os.system('clear')
     print("""
               ---ADMINISTRADOR DATOS DE CLIENTES---
          
                    1. Guardar un cliente nuevo
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
           print(tabulate(postClientes(), headers='keys', tablefmt='fancy grid'))
     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break