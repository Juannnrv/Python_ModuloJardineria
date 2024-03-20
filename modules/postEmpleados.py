import json
import requests
import os
import re
from tabulate import tabulate 
import modules.getEmpleados as gE

def postEmpleado():
    # http://154.38.171.54:5003/empleados
    empleado = dict()
    while True:
        try:
            if not empleado.get('codigo_empleado'):
                while True:
                    codigo = input('Ingresa el código del empleado => ')
                    if codigo.isdigit():
                        data = gE.geAllId(codigo)
                        if (data):
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

            if not empleado.get('puesto'):

                print(""" 
                          1. Subdirector Marketing
                          2. Subdirector Ventas
                          3. Secretari@
                          4. Representante Ventas
                          5. Director Oficina
                      """)
                
                puesto = input('Ingresa número que fue asignado al puesto del empleado => ')
                
                if re.match(r'^[0-9]+$', puesto):
                    puesto = int(puesto)
                    if puesto>=1 and puesto<=5:

                        if puesto == 1:
                            empleado['puesto'] = puesto
                        if puesto == 2:
                            empleado['puesto'] = puesto
                        if puesto == 3:
                            empleado['puesto'] = puesto
                        if puesto == 4:
                            empleado['puesto'] = puesto
                        if puesto == 5:
                            empleado['puesto'] = puesto 
                            
            else:
                raise Exception('No cumple con los estandares establecidos')             
        
        except Exception as error:
            print('---ERROR---')
            print(error)
            break

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5003/empleados", headers=headers, data=json.dumps(empleado))
    res = peticion.json()
    res ['Mensaje'] = 'Empleado Guardado'
    return [res]

def deleteEmpleado(id):
    peticion = requests.delete(f'http://154.38.171.54:5003/empleados/{id}')
    if peticion.status_code == 200:
        print('\nEmpleado eliminado')


def menu():
    os.system('clear')
    while True:
        print("""
               ---ADMINISTRADOR DATOS DE EMPLEADOS---
          
                    1. Guardar un empleado nuevo
                    2. Eliminar un empleado
                    3. Actualizar un empleado existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
        try:
            opcion= int(input('\nSeleccione una de las opciones => '))
            if opcion == 1:
                print(tabulate(postEmpleado(), headers='keys', tablefmt='fancy grid'))
            elif opcion == 2:
                id= input('Ingrese el Id del empleado que desee eliminar => ')
                print(tabulate(deleteEmpleado(id), headers='keys', tablefmt='fancy grid'))
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break

        input('Presiona una tecla para continuar...')        
