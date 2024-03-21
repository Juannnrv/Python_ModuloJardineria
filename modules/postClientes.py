import json
import requests
import os
import re
import modules.getClientes as gC
from tabulate import tabulate

#  Falta put

def postClientes():
    # http://154.38.171.54:5001/cliente

    cliente = dict()
    while True:
        try:
           if(not cliente.get('codigo_cliente')):
                while True:
                    codigo = input('Ingrese el codigo del cliente => ')
                    if (codigo.isdigit()):
                        codigo = int(codigo)
                        data = gC.getAllClientsCodigo(codigo)
                        if(data):
                            raise Exception('El código del cliente ya existe')
                        else:
                            cliente['codigo_cliente'] = codigo
                    else:
                        raise Exception("--> El código no cumple con el estándar establecido")
                    break


           if(not cliente.get('nombre_cliente')):
                nombre = input('Ingrese el nombre del cliente => ')
                if(re.match(r'^[A-Za-z\s]+$', nombre)):
                    cliente['nombre_cliente'] = nombre

           if(not cliente.get('nombre_contacto')):
                nombre = input('Ingrese el nombre de contacto del cliente => ')
                if(re.match(r'^[A-Za-z\s]+$', nombre)):
                    cliente['nombre_contacto'] = nombre  

           if(not cliente.get('apellido_contacto')):
                apellido = input('Ingrese el apellido de contacto del cliente => ')
                if(re.match(r'^[A-Za-z]+$', apellido)):
                    cliente['apellido_contacto'] = apellido
                    
           if(not cliente.get('telefono')):
                telefono = input('Ingrese el telefono del cliente => ')
                if(re.match(r'^\d+(\s*\d+)*$', telefono)):
                    cliente['telefono'] = telefono
        
           if(not cliente.get('fax')):
                fax = input('Ingrese el fax del cliente => ')
                if(re.match(r'^\d+(\s*\d+)*$', fax)):
                    cliente['fax'] = fax     

           if(not cliente.get('linea_direccion1')):
                direccion_1 = input('Ingrese la dirección 1 del cliente => ')
                if(re.match(r'^[^\n]+$', direccion_1)):
                    cliente['direccion_1'] = direccion_1    

           if(not cliente.get('linea_direccion2')):
                direccion_2 = input('Ingrese la dirección 2 del cliente => ')
                if(re.match(r'^[^\n]+$', direccion_2)):
                    cliente['direccion_2'] = direccion_2

           if(not cliente.get('ciudad')):
                ciudad = input('Ingrese la ciudad del cliente => ')
                if(re.match(r'^[A-Za-z\s]+$', ciudad)):
                    cliente['ciudad'] = ciudad

           if(not cliente.get('region')):
                region = input('Ingrese la región del cliente => ')
                if(re.match(r'^[A-Za-z\s]+$', region)):
                    cliente['region'] = region    

           if(not cliente.get('pais')):
                pais = input('Ingrese el país del cliente => ')
                if(re.match(r'^[A-Za-z\s]+$', pais)):
                    cliente['pais'] = pais

           if(not cliente.get('codigo_postal')):
                codigo_postal = input('Ingrese el código postal del cliente => ')
                if(re.match(r'^[0-9]+$', codigo_postal)):
                    cliente['codigo_postal'] = codigo_postal 

           if(not cliente.get('codigo_empleado_rep_ventas')):
                codigo_empleado_rep_ventas = input('Ingrese el código del representante de ventas asignado al cliente => ')
                if codigo_empleado_rep_ventas.isdigit():
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente['codigo_empleado_rep_ventas'] = codigo_empleado_rep_ventas

           if(not cliente.get('limite_credito')):
                limite_credito = input('Ingrese el límite crediticio del cliente => ')
                if re.match(r'^[0-9]+(\.[0-9]+)?$', limite_credito):
                    cliente['limite_credito'] = float(limite_credito)
                    print('\nNuevo cliente guardado :)')

                    break                                 
           
           else:
                raise Exception('No cumple con los estandares establecidos')
            
        except Exception as error:
            print('---ERROR---')
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5001/cliente', headers=headers, data=json.dumps(cliente)) 
    res = peticion.json()
    res ['Mensaje'] = 'Cliente Guardado'
    return [res]

def deleteClient(id):
    peticion = requests.delete(f'http://154.38.171.54:5001/cliente/{id}')
    if peticion.status_code == 200:
        print('\nCliente eliminado satisfactoriamente')

def updateClient(id):
    data = gC.getAllId(id)
    if len(data):
        print("""
                  ¿Qué dato deseas actualizar?

              1. Código del cliente
              2. Nombre del cliente
              3. Nombre de contacto del cliente
              4. Apellido de contacto del cliente
              5. Telefono del cliente
              6. Fax del cliente
              7. Dirección 1 del cliente
              8. Dirección 2 del cliente
              9. Ciudad del cliente
              10. Región del cliente
              11. País del cliente
              12. Código postal del cliente
              13. Representante de ventas del cliente
              14. Límite crediticio del cliente

         Presiona (Ctrl + C) para regresar al menú principal
 """)

    opcion = int(input('Ingresa la opción => '))
    for val in data:
        
        if opcion == 1:
            nuevoCodigo= (input('Ingrese el nuevo código del cliente => '))
            if (re.match(r'^[0-9]+$', nuevoCodigo)):
                nuevoCodigo = int(nuevoCodigo)
                data = data[0]
                data['codigo_cliente'] = nuevoCodigo 

        elif opcion == 2:
            nombre = input('Ingrese el nombre del cliente => ')
            if(re.match(r'^[A-Za-z\s]+$', nombre)):
                data = data[0]
                data['nombre_cliente'] = nombre

        elif opcion == 3:
            nombre = input('Ingrese el nombre de contacto del cliente => ')
            if(re.match(r'^[A-Za-z\s]+$', nombre)):
                data = data[0]
                data['nombre_contacto'] = nombre  

        elif opcion == 4:
            apellido = input('Ingrese el apellido de contacto del cliente => ')
            if(re.match(r'^[A-Za-z]+$', apellido)):
                data = data[0]
                data['apellido_contacto'] = apellido
                    
        elif opcion == 5:   
            telefono = input('Ingrese el telefono del cliente => ')
            if(re.match(r'^\d+(\s*\d+)*$', telefono)):
                data = data[0]
                data['telefono'] = telefono
        
        elif opcion == 6:
            fax = input('Ingrese el fax del cliente => ')
            if(re.match(r'^\d+(\s*\d+)*$', fax)):
                data = data[0]
                data['fax'] = fax     

        elif opcion == 7:
            direccion_1 = input('Ingrese la dirección 1 del cliente => ')
            if(re.match(r'^[^\n]+$', direccion_1)):
                data = data[0]
                data['direccion_1'] = direccion_1    

        elif opcion == 8:
            direccion_2 = input('Ingrese la dirección 2 del cliente => ')
            if(re.match(r'^[^\n]+$', direccion_2)):
                data = data[0]
                data['direccion_2'] = direccion_2

        elif opcion == 9:
            ciudad = input('Ingrese la ciudad del cliente => ')
            if(re.match(r'^[A-Za-z\s]+$', ciudad)):
                data = data[0]
                data['ciudad'] = ciudad

        elif opcion == 10:
            region = input('Ingrese la región del cliente => ')
            if(re.match(r'^[A-Za-z\s]+$', region)):
                data = data[0]
                data['region'] = region    

        elif opcion == 11:
            pais = input('Ingrese el país del cliente => ')
            if(re.match(r'^[A-Za-z\s]+$', pais)):
                data = data[0]
                data['pais'] = pais

        elif opcion == 12:
            codigo_postal = input('Ingrese el código postal del cliente => ')
            if(re.match(r'^[0-9]+$', codigo_postal)):
                data = data[0]
                data['codigo_postal'] = codigo_postal 

        elif opcion == 13:
            codigo_empleado_rep_ventas = input('Ingrese el código del representante de ventas asignado al cliente => ')
            if codigo_empleado_rep_ventas.isdigit():
                data = data[0]
                codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                data['codigo_empleado_rep_ventas'] = codigo_empleado_rep_ventas

        elif opcion == 14:
            limite_credito = input('Ingrese el límite crediticio del cliente => ')
            if re.match(r'^[0-9]+(\.[0-9]+)?$', limite_credito):
                data = data[0]
                data['limite_credito'] = float(limite_credito)
                print('\nNuevo cliente guardado :) ')

        else:
            print('No cumple con los estandares establecidos')

        peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", data=json.dumps(data).encode("UTF-8"))
        res = peticion.json()
        return [res]

# def updateAllCLient(id):
#     cliente = {}
#     data = gC.getAllId(id)
#     if len(data):
            
#         if(not cliente.get('codigo_cliente')):
#             nuevoCodigo= (input('Ingrese el nuevo código del cliente => '))
#             if (re.match(r'^[0-9]+$', nuevoCodigo)):
#                 nuevoCodigo = int(nuevoCodigo)
#                 data = data[0]
#                 data['codigo_cliente'] = nuevoCodigo 

#         if(not cliente.get('nombre_cliente')):
#             nombre = input('Ingrese el nombre del cliente => ')
#             if(re.match(r'^[A-Za-z\s]+$', nombre)):
#                 data = data[0]
#                 data['nombre_cliente'] = nombre

#         if(not cliente.get('nombre_contacto')):
#             nombreC = input('Ingrese el nombre de contacto del cliente => ')
#             if(re.match(r'^[A-Za-z\s]+$', nombreC)):
#                 data = data[0]
#                 data['nombre_contacto'] = nombreC  

#         if(not cliente.get('apellido_contacto')):
#             apellido = input('Ingrese el apellido de contacto del cliente => ')
#             if(re.match(r'^[A-Za-z]+$', apellido)):
#                 data = data[0]
#                 data['apellido_contacto'] = apellido
                    
#         if(not cliente.get('telefono')):
#             telefono = input('Ingrese el telefono del cliente => ')
#             if(re.match(r'^\d+(\s*\d+)*$', telefono)):
#                 data = data[0]
#                 data['telefono'] = telefono
        
#         if(not cliente.get('fax')):
#             fax = input('Ingrese el fax del cliente => ')
#             if(re.match(r'^\d+(\s*\d+)*$', fax)):
#                 data = data[0]
#                 data['fax'] = fax     

#         if(not cliente.get('direccion_1')):
#             direccion_1 = input('Ingrese la dirección 1 del cliente => ')
#             if(re.match(r'^[^\n]+$', direccion_1)):
#                 data = data[0]
#                 data['direccion_1'] = direccion_1    

#         if(not cliente.get('direccion_2')):
#             direccion_2 = input('Ingrese la dirección 2 del cliente => ')
#             if(re.match(r'^[^\n]+$', direccion_2)):
#                 data = data[0]
#                 data['direccion_2'] = direccion_2

#         if(not cliente.get('ciudad')):
#             ciudad = input('Ingrese la ciudad del cliente => ')
#             if(re.match(r'^[A-Za-z\s]+$', ciudad)):
#                 data = data[0]
#                 data['ciudad'] = ciudad

#         if(not cliente.get('region')):
#             region = input('Ingrese la región del cliente => ')
#             if(re.match(r'^[A-Za-z\s]+$', region)):
#                 data = data[0]
#                 data['region'] = region    

#         if(not cliente.get('pais')):
#             pais = input('Ingrese el país del cliente => ')
#             if(re.match(r'^[A-Za-z\s]+$', pais)):
#                 data = data[0]
#                 data['pais'] = pais

#         if(not cliente.get('codigo_postal')):
#             codigo_postal = input('Ingrese el código postal del cliente => ')
#             if(re.match(r'^[0-9]+$', codigo_postal)):
#                 data = data[0]
#                 data['codigo_postal'] = codigo_postal 

#         if(not cliente.get('codigo_empleado_rep_ventas')):
#             codigo_empleado_rep_ventas = input('Ingrese el código del representante de ventas asignado al cliente => ')
#             if codigo_empleado_rep_ventas.isdigit():
#                 data = data[0]
#                 codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
#                 data['codigo_empleado_rep_ventas'] = codigo_empleado_rep_ventas

#         if(not cliente.get('limite_credito')):
#             limite_credito = input('Ingrese el límite crediticio del cliente => ')
#             if re.match(r'^[0-9]+(\.[0-9]+)?$', limite_credito):
#                 data = data[0]
#                 data['limite_credito'] = float(limite_credito)
                


#     peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", data=json.dumps(data).encode("UTF-8"))
#     res = peticion.json()
#     return [res]
# print('\nNuevo cliente guardado :) ')


def menuUpdate():

    print("""
                               ---ACTUALIZACIONES---

              1. Actualizar toda la información de un cliente
              2. Actualizar un dato en especifico de la información del cliente
 """)
    opcion = int(input('\nSelecciona una de las opciones => '))
    
    # if opcion == 1:
    #     idC = input('Ingresa el ID del cliente que deseas actualizar => ')
    #     print(tabulate(updateAllCLient(idC), headers='keys', tablefmt='fancy_grid'))

    if opcion == 2:
        idC = input('Ingresa el ID del cliente que deseas actualizar => ')
        print(tabulate(updateClient(idC), headers='keys', tablefmt='fancy_grid'))


  

    

def menu():
    os.system('clear')
    while True:
     print("""
               ---ADMINISTRADOR DATOS DE CLIENTES---
          
                    1. Guardar un cliente nuevo
                    2. Eliminar un cliente
                    3. Actualizar un cliente existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
            print(tabulate(postClientes(), headers='keys', tablefmt='fancy_grid'))
        if opcion == 2:
            idCliente = input('Ingrese el ID del cliente que desea eliminar => ')
            print(tabulate(deleteClient(idCliente) , headers='keys', tablefmt='fancy_grid'))
        if opcion == 3:
            menuUpdate()

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break