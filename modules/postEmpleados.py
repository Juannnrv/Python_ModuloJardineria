import json
import requests
import os
import re
from tabulate import tabulate 
import modules.getEmpleados as gE

def postEmpleados():
    # http://154.38.171.54:5003/empleados
    empleado = dict()
    while True:
        try:
            if not empleado.get('codigo_empleado'):
                while True:
                    codigo = input('Ingresa el código del empleado => ')
                    if codigo.isdigit():
                        data = gE.getAllCodigoEmpleados(codigo)
                        if data:
                            raise Exception('El código del empleado ya existe')
                        else:
                            empleado['codigo_empleado'] = codigo
                    else:
                        raise Exception("--> El código no cumple con el estándar establecido")
                    break

            if not empleado.get('nombre'):
                nombre = input('Ingrese el nombre del empleado => ')
                if re.match(r'^[A-Za-z]+$', nombre):
                    empleado['nombre'] = nombre

            if not empleado.get('apellido1'):
                apellido1 = input('Ingresa el primer apellido del empleado => ')
                if re.match(r'^[A-Za-z]+$', apellido1):
                    empleado['apellido1'] = apellido1

            if not empleado.get('apellido2'):
                apellido2 = input('Ingresa el segundo apellido del empleado => ')
                if re.match(r'^[A-Za-z]+$', apellido2):
                    empleado['apellido2'] = apellido2

            if not empleado.get('extension'):
                extension = input('Ingresa la extensión del empleado => ')
                if re.match(r'^[0-9]+$', extension):
                    empleado['extension'] = extension
            
            if not empleado.get('email'):
                email = input('Ingresa el email del empleado => ')
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$', email):
                    empleado['email'] = email

            if not empleado.get('codigo_oficina'):
                codigo_oficina = input('Ingresa la codigo de oficina del empleado => ')
                if re.match(r'^[0-9]{2,3}-[0-9]{2,3}$', codigo_oficina):
                    empleado['codigo_oficina'] = codigo_oficina

            if not empleado.get('codigo_jefe'):
                codigo_jefe = input('Ingresa el código del jefe del empleado => ')
                if codigo_jefe.isdigit():
                    empleado['codigo_jefe'] = codigo_jefe

# TERMINAR DE ENUMERAR LOS PUESTOS PARA PODER ELEGIRLOS

            if not empleado.get('puesto'):
                print('1. ')
                puesto = input('Ingresa el puesto del empleado => ')
                empleado['puesto'] = puesto

                if puesto != getAllPuesto:
                    print('Ningun empleado asign')
            




        except Exception as error:
            print('---ERROR---')
            print(error)
            break




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
    peticion = requests.post('http://154.38.171.54:5003/empleados', headers=headers, data=json.dumps(Empleado))
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