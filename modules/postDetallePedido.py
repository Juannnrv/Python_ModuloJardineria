import json
import requests
import os
import re
import modules.getDetallePedido as gD
from tabulate import tabulate

def postDetallePedido():

    # http://154.38.171.54:5002/detalle_pedido

    detallePedido = dict()
    while True:
        try:
           if(not detallePedido.get('codigo_pedido')):
                while True:
                    codigo = input('Ingrese el codigo asignado al detalle del pedido => ')
                    if (codigo.isdigit()):
                        codigo = int(codigo)
                        data = gD.getAllCodigos(codigo)
                        if(data):
                            raise Exception('El código del pedido ya existe')
                        else:
                            detallePedido['codigo_cliente'] = codigo
                    else:
                        raise Exception("--> El código no cumple con el estándar establecido")
                    break

                codigo_producto = input('Ingrese el código del producto => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{2,3}+$', codigo_producto)):
                    detallePedido['codigo_producto'] = codigo_producto

                cantidad = input('Ingrese la cantidad => ')
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    detallePedido['cantidad'] = cantidad

                precio_unidad = input('Ingrese el precio de unidad => ')
                if precio_unidad.isdigit():
                    precio_unidad = float(precio_unidad)
                    detallePedido['precio_unidad'] = precio_unidad

                numero_linea = input('Ingrese el número en linea => ')
                if numero_linea.isdigit():
                    numero_linea = int(numero_linea)
                    detallePedido['numero_linea'] = numero_linea
                    break
           
                else:
                    print('No cumple con los estandares')

        except Exception as error:
            print('---ERROR---')
            print(error)
            break
    
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5002/detalle_pedido', headers=headers, data=json.dumps(detallePedido))
    res = peticion.json()
    res ['Mensaje'] = 'Detalles de producto Guardado'
    return [res]

def deleteDetallePedido(id):
    peticion = requests.delete(f'http://154.38.171.54:5002/detalle_pedido/{id}')
    if peticion.status_code == 200:
        print('\nDetalle de producto eliminado satisfactoriamente')

def updateDetallePedido(id):
    data = gD.getAllId(id)
    if len(data):
        print("""
                  ¿Qué dato deseas actualizar?

                    1. Código de pedido
                    2. Código del producto
                    3. Cantidad
                    4. Precio por unidad
                    5. Número en linea
              
         Presiona (Ctrl + C) para regresar al menú principal
 """)
        opcion = int(input('Ingresa la opción => '))
        for val in data:

            if opcion == 1:
                codigo_pedido = input('Ingrese el código del pedido => ')
                if codigo_pedido.isdigit():
                    codigo_pedido = int(codigo_pedido)
                    data = data[0]
                    data['codigo_pedido'] = codigo_pedido

            elif opcion == 2:
                codigo_producto = input('Ingrese el código del producto => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{2,3}+$', codigo_producto)):
                    data = data[0]
                    data['codigo_producto'] = codigo_producto

            elif opcion == 3:
                cantidad = input('Ingrese la cantidad del pedido => ')
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    data = data[0]
                    data['cantidad'] = cantidad

            elif opcion == 4:
                precio_unidad = input('Ingrese el precio por unidad del pedido => ')
                if precio_unidad.isdigit():
                    precio_unidad = float(precio_unidad)
                    data = data[0]
                    data['precio_unidad'] = precio_unidad

            elif opcion == 5:
                numero_linea = input('Ingrese el número de linea del pedido => ')
                if numero_linea.isdigit():
                    numero_linea = int(numero_linea)
                    data = data[0]
                    data['numero_linea'] = numero_linea

            else:
                print('No cumple con los estandares establecidos')

    peticion = requests.put(f"http://154.38.171.54:5002/detalle_pedido/{id}", data=json.dumps(data).encode("UTF-8"))
    res = peticion.json()
    return [res]

def menu():
    while True:
     os.system('clear')
     print("""
            ---ADMINISTRADOR DATOS DE DETALLES DE PEDIDO---
          
                    1. Guardar un detalle de pedido nuevo
                    2. Eliminar un detalle de pedido
                    3. Actualizar un detalle de pedido existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
            print(tabulate(postDetallePedido(), headers='keys', tablefmt='fancy_grid'))
        if opcion == 2:
            idCliente = input('Ingrese el ID del cliente que desea eliminar => ')
            print(tabulate(deleteDetallePedido(idCliente) , headers='keys', tablefmt='fancy_grid'))
        if opcion == 3:
            idCliente = input('Ingrese el ID del cliente que desea actualizar => ')
            print(tabulate(updateDetallePedido(idCliente) , headers='keys', tablefmt='fancy_grid'))

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break
     
     input('presion la tecla Enter para continuar...')