import json
import requests
import os
import re
import modules.getOficina as gO
from tabulate import tabulate


def postOficina():
    # json-server storage/oficina.json -b 5502
    
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
            
            
    # headers = {'Content-Type': 'application/json', 'charser': 'UTF-8'}
    # peticion = requests.post('http://192.168.1.7:5502', headers=headers, data=json.dumps(oficina))
    # res = peticion.json()
    # res ['Mensaje'] = 'Oficina Guardada'
    # return [res]


def menu():
    while True:
        os.system('clear')
        print("""
               ---ADMINISTRADOR DATOS DE LAS OFICINAS---
          
                    1. Guardar un oficina nueva
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
        try:
            opcion = int(input('\nSeleccione una de las opciones => '))
            if opcion == 1:
               print(postOficina())
            #    input('Por favor presione una tecla para continuar... ')
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break