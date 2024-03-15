import json
import requests
import os
from tabulate import tabulate 

def postEmpleados():

    Empleado = {

        "codigo_empleado": int(input('Ingrese el codigo del empleado => ')),
        "nombre": input('Ingrese el nombre => '),
        "apellido1": input('Ingrese el primer apellido => '),
        "apellido2": input('Ingrese el segundo apellido => '),
        "extension": input('Ingrese la extensión => '),
        "email": input('Ingrese el email => '),
        "codigo_oficina": input('Ingrese el código de oficina => '),
        "codigo_jefe": int(input('Ingrese el codigo del jefe => ')),
        "puesto": input('Ingrese el puesto => ')
    }

    headers = {'Content Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://172.16.106.67:5006', headers=headers, data=json.dumps(Empleado))
    res = peticion.json()
    res ['Mensaje'] = 'Cliente Guardado'
    return [res]

def menu():
    while True:
        os.system('clear')
        print("""
               ---ADMINISTRADOR DATOS DE EMPLEADOS---
          
                    1. Guardar un empleado nuevo
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
        try:
            opcion= int(input('\nSelccione una de las opciones => '))
            if opcion == 1:
                print(tabulate(postEmpleados(), headers='keys', tablefmt='fancy grid'))
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break        