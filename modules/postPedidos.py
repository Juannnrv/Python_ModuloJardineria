import json
import requests
import os
import re
import modules.getPedidos as gP
from tabulate import tabulate

def postPedidos():
     # http://154.38.171.54:5007/pedidos
    pedido = {}
    while True:
        try:
           if(not pedido.get('codigo_pedido')):
                while True:
                    codigo = input('Ingrese el codigo del pedido => ')
                    if (codigo.isdigit()):
                        codigo = int(codigo)
                        data = gP.getAllCodigo(codigo)
                        if(data):
                            raise Exception('El código del pedido ya existe')
                        else:
                            pedido['codigo_pedido'] = codigo
                    else:
                        raise Exception("--> El código no cumple con el estándar establecido")
                    break


           if(not pedido.get('fecha_pedido')):
                fecha_pedido = input('Ingrese la fecha de pedido => ')
                if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_pedido)):
                    pedido['fecha_pedido'] = fecha_pedido

           if not pedido.get('fecha_esperada'):
                fecha_esperada = input('Ingrese la fecha de espera => ')
                if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_esperada)):
                    pedido['fecha_esperada'] = fecha_esperada

           if not pedido.get('fecha_entrega'):
                fecha_entrega = input('Ingrese la fecha de entrega => ')
                if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_entrega)):
                    pedido['fecha_entrega'] = fecha_entrega

           if not pedido.get('estado'):
                estado = input('Ingrese el estado del pedido => ')
                if(re.match(r'^[A-Za-z]+$', estado)):
                    pedido['estado'] = estado

           if not pedido.get('comentario'):
                comentario = input('Ingrese el comentario del pedido => ')
                if(re.match(r'^[^\n]+$', comentario)):
                    pedido['comentario'] = comentario

           if not pedido.get('codigo_cliente'):
                codigo_cliente = input('Ingrese el nombre del cliente => ')
                if codigo_cliente.isdigit():
                    codigo_cliente = int(codigo_cliente)
                    pedido['codigo_cliente'] = codigo_cliente
                break
           else:
                raise Exception('No cumple con los estandares establecidos')
            
        except Exception as error:
            print('---ERROR---')
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5007/pedidos', headers=headers, data=json.dumps(pedido)) 
    res = peticion.json()
    res ['Mensaje'] = 'Pedido Guardado'
    return [res]


def deletePedido(id):
    peticion = requests.delete(f'http://154.38.171.54:5007/pedidos/{id}')
    if peticion.status_code == 200:
        print('\nPedido eliminado satisfactoriamente')

def updatePedido(id):
    data = gP.getAllId(id)
    if len(data):
        print("""
            ¿Qué dato deseas actualizar?

              1. Código de pedido
              2. Fecha de pedido
              3. Fecha de espera
              4. Fecha de entrega
              5. Estado del pedido
              6. Comentario del pedido
              7. Código del cliente
              
         Presiona (Ctrl + C) para regresar al menú principal
 """)
        opcion = int(input('Selecciona un opción => '))

        if opcion == 1:
            codigo = input('Ingrese el nuevo código del pedido => ')
            if codigo.isdigit():
                codigo = int(codigo)
                data = data[0]
                data['codigo_pedido'] = codigo

        if codigo == 2:
            fecha_pedido = input('Ingrese la nueva fecha de pedido => ')
            if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_pedido)):
                data = data[0]
                data['fecha_pedido'] = fecha_pedido

        if opcion == 3:
            fecha_esperada = input('Ingrese la nueva fecha de espera => ')
            if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_esperada)):
                data = data[0]
                data['fecha_esperada'] = fecha_esperada

        if opcion == 4:
            fecha_entrega = input('Ingrese la nueva fecha de entrega => ')
            if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_entrega)):
                data = data[0]
                data['fecha_entrega'] = fecha_entrega

        if opcion == 5:
            comentario = input('Ingresa el nuevo comentario del pedido => ')
            if(re.match(r'^[^\n]+$', comentario)):
                data = data[0]
                data['comentario'] = comentario

        if opcion == 6:
            codigo_cliente = input('Ingrese el nuevo código del cliente => ')
            if codigo_cliente.isdigit():
                codigo_cliente = int(codigo_cliente)
                data = data[0]
                data['codigo_cliente'] = codigo_cliente

        else:
            print('No cumple con los estandares establecidos')

        peticion = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(data).encode("UTF-8"))
        res = peticion.json()
        return [res]
    
def menu():
    while True:
     os.system('clear')
     print("""
               ---ADMINISTRADOR DATOS DE PEDIDOS---
          
                    1. Guardar un pedido nuevo
                    2. Eliminar un pedido
                    3. Actualizar un pedido existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
            print(tabulate(postPedidos(), headers='keys', tablefmt='fancy_grid'))
        if opcion == 2:
            idCliente = input('Ingrese el ID del pago que desea eliminar => ')
            print(tabulate(deletePedido(idCliente) , headers='keys', tablefmt='fancy_grid'))
        if opcion == 3:
            id = input('Ingrese el ID del pago que desea actualizar => ')
            print(tabulate(updatePedido(id), headers='keys', tablefmt='fancy_grid'))

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break
     
     input('Presione la tecla Enter para poder continuar...')
        