import json
import requests
import os
import re
import modules.getOficina as gO
from tabulate import tabulate


def postOficina():
    # json-server storage/oficina.json -b 5007
    
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
                if ciudad[0].isupper() and ciudad[1:].isalpha(): 
                    oficina['ciudad'] = ciudad

            if not oficina.get('pais'):
                pais = input('Ingrese el país de la oficina => ')
                if ciudad[0].isupper() and ciudad[1:].isalpha():
                    oficina['pais'] = pais

            if not oficina.get('region'):
                region = input('Ingrese la region de la oficina => ')
                if ciudad[0].isupper() and ciudad[1:].isalpha():
                    oficina['region'] = region

            if not oficina.get('codigo_postal'):
                codigo_postal = input('Ingrese el código postal de la oficina => ')
                if re.match(r'^[0-9]{5}|[A-Z0-9]{4}\s[A-Z0-9]{3}|[A-Z]{3}\s[0-9]{4}|[0-9]{3}-[0-9]{4}$', codigo_postal):
                    oficina['codigo_postal'] = codigo_postal

        except Exception as error:
            print('---ERROR---')
            print(error)
            
    headers = {'Content-Type': 'application/json', 'charser': 'UTF-8'}
    peticion = requests.post('http://192.168.1.7:5502', headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res ['Mensaje'] = 'Oficina Guardada'
    return [res]


def menu():
    while True:
        os.system('clear')
        print("""
               ---ADMINISTRADOR DATOS DE LAS OFICINAS---
          
                    1. Guardar un oficina nueva
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
        try:
            opcion = input('\nSeleccione una de las opciones => ')
            if opcion == 1:
                print(tabulate(postOficina(), headers='keys', tablefmt='fancy grid'))
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break