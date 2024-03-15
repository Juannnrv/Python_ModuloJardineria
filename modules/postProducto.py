import json
import requests
import os
import re
import modules.getProducto as gP
from tabulate import tabulate

def postProducto():
    #json-server storage/producto.json -b 5502
    producto = dict()
    while True:
        try:
            if(not producto.get('codigo_producto')):
                codigo = input('Ingrese el codigo del producto => ')
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                    data = gP.getProductoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers='keys', tablefmt='fancy grid'))
                        raise Exception('El código no cumple con los estándar establecido')
                    else:
                        producto['codigo_producto'] = codigo
                else:
                    raise Exception('El código no cumple con el estándar establecido')
                
            if(not producto.get('nombre')):
                nombre = input('Ingrese el nombre del producto => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', nombre) is not None):
                    producto['nombre'] = nombre
                    break
            else:
                raise Exception('El nombre del producto no cumple con el estándar establecido')
        except ValueError as error:
            print('ERROR')
            print(error)

    




    """producto = {
             'codigo_producto': input('Ingrese el codigo del producto => '),
             'nombre': input('Ingrese el nombre del producto => '),
             'gama': input('Ingrese la gama del producto => '),
             'dimensiones': input('Ingrese las dimensiones del producto => '),
             'proveedor': input('Ingrese el proveedor del producto => '),
             'descripcion': input('Ingrese la descripcion del producto => '),
             'cantidad_en_stock': int(input('Ingrese la cantidad en stock del producto => ')),
             'precio_venta': int(input('Ingrese el precio de venta del producto => ')),
             'precio_proveedor': int(input('Ingrese el precio del producto'))
         }"""
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.116:5502", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res ['Mensaje'] = 'Producto Guardado'
    return [res]

def menu():
    while True:
     os.system('clear')
     print("""
               ---ADMINISTRADOR DATOS DE PRODUCTOS---
          
                    1. Guardar un producto nuevo
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
           print(tabulate(postProducto(), headers='keys', tablefmt='fancy grid'))
           input('Por favor presione una tecla para continuar... ')
     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break 
