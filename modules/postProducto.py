import json
import requests
import os
import re
import modules.getProducto as gP
from tabulate import tabulate

def postProducto():
    #json-server storage/producto.json -b 5506
    producto = dict()
    while True:
        try:
            if(not producto.get('codigo_producto')):
                while True:
                    codigo = input('Ingrese el codigo del producto => ')
                    if ((re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None) or (codigo.isdigit())):
                        data = gP.getProductoCodigo(codigo)
                        if(data):
                            raise Exception('El código del producto ya existe')
                        else:
                            producto['codigo_producto'] = codigo
                    else:
                        raise Exception("--> El código no cumple con el estándar establecido")
                    break
                
            if(not producto.get('nombre')):
                nombre = input('Ingrese el nombre del producto => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', nombre) is not None):
                    producto['nombre'] = nombre
            
            if(not producto.get('gama')):
                gama = input('Ingrese la gama del producto => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', gama) is not None):
                         producto['gama'] = gama
                    
            if(not producto.get('dimensiones')):
                dimensiones = input('Ingrese las dimensiones del producto => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', dimensiones) is not None):
                    producto['dimensiones'] = dimensiones

            if (not producto.get('proveedor')):
                proveedor = input('Ingrese los datos del proveedor => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', proveedor) is not None):
                    producto['proveedor'] = proveedor

            if (not producto.get('descripcion')):
                descripcion = input('Ingresa la descripcion del producto')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', dimensiones) is not None):
                    producto['dimensiones'] = descripcion

            if(not producto.get('cantidad_en_stock')):
                cantidad_en_stock = (input('Ingrese la cantidad de stock'))
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$', cantidad_en_stock) is not None):
                    cantidad_en_stock = int(cantidad_en_stock)
                    producto['cantidad_en_stock'] = cantidad_en_stock  

            if(not producto.get('precio_venta')):
                precio_venta = (input('Ingrese el precio de venta del producto'))
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$', precio_venta) is not None):
                    precio_venta = int(precio_venta)
                    producto['precio_venta'] = precio_venta

            if(not producto.get('precio_proveedor')):
                precio_proveedor = (input('Ingrese el precio de venta del producto'))
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$', precio_proveedor) is not None):
                    precio_proveedor = int(precio_proveedor)
                    producto['precio_proveedor'] = precio_proveedor
                    break 

            else:
                raise Exception('No cumple con los estandares establecidos')
            
        except Exception as error:
            print('---ERROR---')
            print(error)
        
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://192.168.1.7:5506", headers=headers, data=json.dumps(producto))
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
        #    
           print(postProducto())
           input('Por favor presione una tecla para continuar... ')
     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break 
