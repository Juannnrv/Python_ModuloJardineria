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
                    precio_venta = int(precio_venta)
                    producto['precio_venta'] = precio_venta

            if(not producto.get('precio_proveedor')):
                precio_proveedor = (input('Ingrese el precio del producto asignado por el proveedor => '))
                if precio_proveedor.isdigit():
                    precio_proveedor = int(precio_proveedor)
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

def updateProducto(id):
    data = gP.getAllId(id)
    if len(data):
        print("""
            ¿Qué dato deseas actualizar?

              1. Código del producto
              2. Nombre del producto
              3. Gama del producto
              4. Dimensiones del producto
              5. Proveedor del producto
              6. Descripción del producto
              7. Cantidad en stock del producto
              8. Precio de venta del producto
              9. Precio proveedor del producto
              
         Presiona (Ctrl + C) para regresar al menú principal
 """)
        opcion = input('\nIngresa una opción => ')
        
        if opcion == 1:
            nuevoCodigo= (input('Ingrese el nuevo código del cliente => '))
            if ((re.match(r'^[A-Z]{2}-[0-9]{2,3}$', nuevoCodigo)) or (nuevoCodigo.isdigit())):
                        nuevoCodigo = int(nuevoCodigo)
                        data = data[0]
                        data['codigo_cliente'] = nuevoCodigo 
                    
        elif opcion == 2:
            nombre = input('Ingrese el nombre del producto => ')
            if(re.match(r'^[A-Za-z\s]+$', nombre)):
                        data = data[0]
                        data['nombre'] = nombre
                
        elif opcion == 3:
            gama = input('Ingrese la gama del producto => ')
            if re.match(r'^[A-Za-z]+$', gama):
                        data = data[0]        
                        data['gama'] = gama
                        
        elif opcion == 4:
            dimensiones = input('Ingrese las dimensiones del producto => ')
            if re.match(r'^[0-9]{1,3}-[0-9]{1,3}$', dimensiones):
                        data = data[0]
                        data['dimensiones'] = dimensiones

        elif opcion == 5:
            proveedor = input('Ingrese el nombre del proveedor => ')
            if re.match(r'^[A-Za-z\s]+$', proveedor):
                        data = data[0]
                        data['proveedor'] = proveedor

        elif opcion == 6:
            descripcion = input('Ingresa la descripcion del producto => ')
            if re.match(r'^[^\n]+$', descripcion):
                        data = data[0]
                        data['descripcion'] = descripcion

        elif opcion == 7:
            cantidad_en_stock = (input('Ingrese la cantidad en stock => '))
            if cantidad_en_stock.isdigit():
                        cantidad_en_stock = int(cantidad_en_stock)
                        data = data[0]
                        data['cantidad_en_stock'] = cantidad_en_stock  

        elif opcion == 8:
            precio_venta = (input('Ingrese el precio de venta del producto => '))
            if precio_venta.isdigit():
                        precio_venta = int(precio_venta)
                        data = data[0]
                        data['precio_venta'] = precio_venta

        elif opcion == 9:
            precio_proveedor = (input('Ingrese el precio del producto asignado por el proveedor => '))
            if precio_proveedor.isdigit():
                        precio_proveedor = int(precio_proveedor)
                        data = data[0]
                        data['precio_proveedor'] = precio_proveedor 

        # else:
        #     print('No cumple con los estandares establecidos')
                
        peticion = requests.put(f"http://154.38.171.54:5008/productos/{id}", data=json.dumps(data[0]).encode("UTF-8"))
        res = peticion.json()
        return [res]
                


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
           print(tabulate(postProducto(), headers='keys', tablefmt='fancy_grid'))

        elif opcion == 2:
           idProductoDele = input('Ingrese el id del producto que deseas eliminar => ')
           print(tabulate(deleteProducto(idProductoDele), headers='keys', tablefmt='fancy_grid')) # Aún asi funciona

        elif opcion == 3:
           idPro = input('Ingrese el id del producto el cual deseas actualizar => ')
           print(tabulate(updateProducto(idPro), headers= "keys", tablefmt='fancy_grid'))

        input('Presione una tecla para continuar...')

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break 
     
    input('Presione una tecla para continuar...')
