import json
import requests
import os
import re
import modules.getPagos as gP
from tabulate import tabulate

def postPagos():

    # http://154.38.171.54:5006/pagos

    pago = {}
    while True:
        try:
           if(not pago.get('codigo_cliente')):
                while True:
                    codigo = input('Ingrese el codigo del cliente => ')
                    if (codigo.isdigit()):
                        codigo = int(codigo)
                        data = gP.getAllClientsCodigo(codigo)
                        if(data):
                            raise Exception('El código del cliente ya existe')
                        else:
                            pago['codigo_cliente'] = codigo
                    else:
                        raise Exception("--> El código no cumple con el estándar establecido")
                    break


           if(not pago.get('forma_pago')):
                forma_pago = input('Ingrese la forma de pago => ')
                if(re.match(r'^[A-Za-z]+$', forma_pago)):
                    pago['forma_pago'] = forma_pago

           if not pago.get('id_transaccion'):
                id_transaccion = input('Ingrese el id de la transacción => ')
                if(re.match(r'^[a-z]{2}-[a-z]{3}-[0-9]{6}+$', id_transaccion)):
                    pago['id_transaccion'] = id_transaccion

           if not pago.get('fecha_pago'):
                fecha_pago = input('Ingrese la fecha de pago => ')
                if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_pago)):
                    pago['fecha_pago'] = fecha_pago

           if not pago.get('total'):
                total = input('Ingrese el total del pago => ')
                if total.isdigit():
                    total = int(total)
                    pago['total'] = total
                    break

           else:
                raise Exception('No cumple con los estandares establecidos')
            
        except Exception as error:
            print('---ERROR---')
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5006/pagos', headers=headers, data=json.dumps(pago)) 
    res = peticion.json()
    res ['Mensaje'] = 'Cliente Guardado'
    return [res]

def deletePagos(id):
    peticion = requests.delete(f'http://154.38.171.54:5006/pagos/{id}')
    if peticion.status_code == 200:
        print('\nCliente eliminado satisfactoriamente')

def updatePagos(id):
    data = gP.getAllId(id)
    if len(data):
        print("""
            ¿Qué dato deseas actualizar?

              1. Código de cliente
              2. Forma de pago
              3. Id de la transacción del pago
              4. Fecha del pago
              5. Total del pago
              
         Presiona (Ctrl + C) para regresar al menú principal
 """)
        opcion = int(input('Ingresa la opción => '))

        if opcion == 1:
            nuevoCodigo= (input('Ingrese el nuevo código del cliente => '))
            if nuevoCodigo.isdigit():
                nuevoCodigo = int(nuevoCodigo)
                data = data[0]
                data['codigo_cliente'] = nuevoCodigo 

        if opcion == 2:
            forma_pago = input('Ingrese la forma de pago => ')
            if(re.match(r'^[A-Za-z]+$', forma_pago)):
                data = data[0]
                data['forma_pago'] = forma_pago

        if opcion == 3:
            id_transaccion = input('Ingrese el id de la transacción => ')
            if(re.match(r'^[a-z]{2}-[a-z]{3}-[0-9]{6}+$', id_transaccion)):
                data = data[0]
                data['id_transaccion'] = id_transaccion

        if opcion == 4:
            fecha_pago = input('Ingrese la fecha de pago => ')
            if(re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$', fecha_pago)):
                data = data[0]
                data['fecha_pago'] = fecha_pago

        if opcion == 5:
            total = input('Ingrese el total del pago => ')
            if total.isdigit():
                total = int(total)
                data = data[0]
                data['total'] = total

        else:
            print('No cumple con los estandares establecidos')

        peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", data=json.dumps(data).encode("UTF-8"))
        res = peticion.json()
        return [res]

def menu():
    os.system('clear')
    while True:
     print("""
               ---ADMINISTRADOR DATOS DE PAGOS---
          
                    1. Guardar un pago nuevo
                    2. Eliminar un pago
                    3. Actualizar un pago existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
            print(tabulate(postPagos(), headers='keys', tablefmt='fancy_grid'))
        if opcion == 2:
            idCliente = input('Ingrese el ID del pago que desea eliminar => ')
            print(tabulate(deletePagos(idCliente) , headers='keys', tablefmt='fancy_grid'))
        if opcion == 3:
            id = input('Ingrese el ID del pago que desea actualizar => ')
            print(tabulate(updatePagos(id), headers='keys', tablefmt='fancy_grid'))

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break