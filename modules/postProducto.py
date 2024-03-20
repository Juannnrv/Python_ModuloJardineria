import json
import requests
import os
import re
import modules.getProducto as gP
from tabulate import tabulate

def postProducto():
    # http://154.38.171.54:5008/productos
    producto = dict()
    while True:
        try:
            if(not producto.get('codigo_producto')):
                while True:
                    codigo = input('Ingrese el codigo del producto => ')
                    if ((re.match(r'^[A-Z]{2}-[0-9]{2,3}$', codigo) is not None) or (codigo.isdigit())):
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
                if(re.match(r'^[A-Za-z\s]+$', nombre)):
                    producto['nombre'] = nombre
            
            if(not producto.get('gama')):
                gama = input('Ingrese la gama del producto => ')
                if(re.match(r'^[A-Za-z]+$', gama) is not None):
                    producto['gama'] = gama
                    
            if(not producto.get('dimensiones')):
                dimensiones = input('Ingrese las dimensiones del producto => ')
                if(re.match(r'^[0-9]{1,3}-[0-9]{1,3}$', dimensiones) is not None):
                    producto['dimensiones'] = dimensiones

            if (not producto.get('proveedor')):
                proveedor = input('Ingrese el nombre del proveedor => ')
                if(re.match(r'^[A-Za-z\s]+$', proveedor) is not None):
                    producto['proveedor'] = proveedor

            if (not producto.get('descripcion')):
                descripcion = input('Ingresa la descripcion del producto => ')
                if(re.match(r'^[^\n]+$', descripcion) is not None):
                    producto['descripcion'] = descripcion

            if(not producto.get('cantidad_en_stock')):
                cantidad_en_stock = (input('Ingrese la cantidad en stock => '))
                if cantidad_en_stock.isdigit():
                    producto['cantidad_en_stock'] = cantidad_en_stock  

            if(not producto.get('precio_venta')):
                precio_venta = (input('Ingrese el precio de venta del producto => '))
                if precio_venta.isdigit():
                    producto['precio_venta'] = precio_venta

            if(not producto.get('precio_proveedor')):
                precio_proveedor = (input('Ingrese el precio del producto asignado por el proveedor => '))
                if precio_proveedor.isdigit():
                    producto['precio_proveedor'] = precio_proveedor
                    break 

            else:
                raise Exception('No cumple con los estandares establecidos')
            
        except Exception as error:
            print('---ERROR---')
            print(error)
            break
        
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5008/productos", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res ['Mensaje'] = 'Producto Guardado'
    return [res]

def deleteProducto(id):
    peticion = requests.delete(f'http://154.38.171.54:5008/productos/{id}')
    if peticion.status_code == 200:
        print('\nProducto eliminado')



def menu():
    while True:
     os.system('clear')
     print("""
               ---ADMINISTRADOR DATOS DE PRODUCTOS---
          
                    1. Guardar un producto nuevo
                    2. Eliminar un producto 
                    3. Actualizar un producto existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        
        opcion = int(input('\nSeleccione una de las opciones => '))

        if opcion == 1:
           print(tabulate(postProducto(), headers='keys', tablefmt='fancy grid'))

        elif opcion == 2:
           idProductoDele = input('Ingrese el id del producto que deseas eliminar => ')
           print(tabulate(deleteProducto(idProductoDele), headers='keys', tablefmt='fancy grid')) # Aún asi funciona

        # elif opcion == 3:
        #     idProductoUpt = input('Ingrese el id del producto el cual deseas actualizar => ')
        #     print(tabulate(updateProducto(idProductoUpt)['body'], headers= "keys", tablefmt='fancy grid'))

        input('Presione una tecla para continuar...')

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break 
     
    input('Presione una tecla para continuar...')
