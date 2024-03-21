import json
import requests
import os
import re
import modules.getOficina as gO
from tabulate import tabulate


def postOficina():
    # http://154.38.171.54:5005/oficinas
    
    oficina = dict()
    while True:
        try:
            if not oficina.get('codigo_oficina'):
                while True:
                    codigo = input('Ingrese el código de la oficina => ')
                    if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo):
                        data = gO.getOficinaCodigo(codigo)
                        if (data):
                            raise Exception('El código de la oficina ya existe')
                        else:
                            oficina['codigo_oficina'] = codigo
                    else:
                        raise Exception('El código no cumple con el estándar establecido')
                    break  

            if not oficina.get('ciudad'):
                ciudad = input('Ingrese la ciudad de la oficina => ')
                if re.match(r'^[A-Za-z\s]$', ciudad): 
                    oficina['ciudad'] = ciudad

            if not oficina.get('pais'):
                pais = input('Ingrese el país de la oficina => ')
                if re.match(r'^[A-Za-z]$', pais):
                    oficina['pais'] = pais

            if not oficina.get('region'):
                region = input('Ingrese la región de la oficina => ')
                if re.match(r'^[A-Za-z\s-]+$', region):
                    oficina['region'] = region

            if not oficina.get('codigo_postal'):
                codigo_postal = input('Ingrese el código postal de la oficina => ')
                if re.match(r'^[a-zA-Z\w\s-]+$', codigo_postal):
                    oficina['codigo_postal'] = codigo_postal

            if not oficina.get('telefono'):
                telefono = input('Ingrese el teléfono de la oficina => ')
                if re.match(r'^\+\d+(\s\d+)*$', telefono):
                    oficina['telefono'] = telefono

            if not oficina.get('linea_direccion1'):
                linea_direccion1 = input('Ingrese la dirección 1 de la oficina => ')
                if re.match(r'^[^\n]+$', linea_direccion1):
                    oficina['linea_direccion1'] = linea_direccion1

            if not oficina.get('linea_direccion2'):
                linea_direccion2 = input('Ingrese la dirección 2 de la oficina => ')
                if re.match(r'^[^\n]+$', linea_direccion2):
                    oficina['linea_direccion2'] = linea_direccion2
                    break
                
            else:
                raise Exception('No cumple con los estandares establecidos')
            

        except Exception as error:
            print('---ERROR---')
            print(error)
            
            
    headers = {'Content-Type': 'application/json', 'charser': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5005/oficinas', headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res ['Mensaje'] = 'Oficina Guardada'
    return [res]

def deleteOficina(id):
    peticion = requests.delete(f'http://154.38.171.54:5005/oficinas/{id}')
    if peticion.status_code == 200:
        print('\nOficina eliminado')


def updateOficina(id):
    data = gO.getAllId(id)
    if len(data):
        print("""
                ¿Qué dato deseas actualizar?

              1. Código de la oficina
              2. Ciudad de la oficina
              3. País de la oficina
              4. Región de la oficina
              5. Código postal de la oficina
              6. Telefono de la oficina
              7. Primera linea de dirección de la oficina
              8. Segunda linea de dirección de la oficina
              

       Presiona (Ctrl + C) para regresar al menú principal
              
 """)
    opcion = int(input('\nSeleccione una opción => '))
    for val in data:
        if opcion == 1:
            codigo = input('Ingresa el código de la oficina => ')
            if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo):
                datamod = data[0]
                datamod['codigo_oficina'] = codigo

        elif opcion == 2:
            ciudad = input('Ingrese la ciudad de la oficina => ')
            if re.match(r'^[A-Za-z\s]+$', ciudad): 
                datamod = data[0]
                datamod['ciudad'] = ciudad

        elif opcion == 3:
            pais = input('Ingrese el país de la oficina => ')
            if re.match(r'^[A-Za-z]+$', pais):
                datamod = data[0]
                datamod['pais'] = pais

        elif opcion == 4:
            region = input('Ingrese la región de la oficina => ')
            if re.match(r'^[A-Za-z\s-]+$', region):
                datamod = data[0]
                datamod['region'] = region

        elif opcion == 5:
            codigo_postal = input('Ingrese el código postal de la oficina => ')
            if re.match(r'^[a-zA-Z\w\s-]+$', codigo_postal):
                datamod = data [0]
                datamod['codigo_postal'] = codigo_postal

        elif opcion == 6:
            telefono = input('Ingrese el teléfono de la oficina => ')
            if re.match(r'^\+\d+(\s\d+)*$', telefono):
                datamod = data[0]
                datamod['telefono'] = telefono

        elif opcion == 7:
            linea_direccion1 = input('Ingrese la dirección 1 de la oficina => ')
            if re.match(r'^[^\n]+$', linea_direccion1):
                datamod = data[0]
                datamod['linea_direccion1'] = linea_direccion1

        elif opcion == 8:
            linea_direccion2 = input('Ingrese la dirección 2 de la oficina => ')
            if re.match(r'^[^\n]+$', linea_direccion2):
                    datamod = data[0]
                    datamod['linea_direccion2'] = linea_direccion2

        else:
            print('No cumple con los estandares establecidos')
    
    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{id}', data=json.dumps(data[0]).encode("UTF-8"))
    res = peticion.json()
    return [res]


def menu():
    os.system('clear')
    while True:
        print("""
               ---ADMINISTRADOR DATOS DE LAS OFICINAS---
          
                    1. Guardar un oficina nueva
                    2. Eliminar una oficina
                    3. Actualizar un empleado existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
        try:
            opcion = int(input('\nSeleccione una de las opciones => '))
            if opcion == 1:
               print(tabulate(postOficina(), headers='keys', tablefmt='fancy_grid'))
            if opcion == 2:
               idO = ('Ingresa el ID del empleado que desee actualizar => ')
               print(tabulate(deleteOficina(idO), headers='keys', tablefmt='fancy_grid'))
            if opcion == 3:
               idE = input('Ingresa el ID del empleado que desee actualizar => ')
               print(tabulate(updateOficina(idE), headers='keys', tablefmt='fancy_grid'))
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break

        input('Por favor presione una tecla para continuar... ')