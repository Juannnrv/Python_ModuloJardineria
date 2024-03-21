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
                        codigo = int(codigo)
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

            elif not empleado.get('apellido1'):
                apellido1 = input('Ingresa el primer apellido del empleado => ')
                if re.match(r'^[A-Za-z]+$', apellido1):
                    empleado['apellido1'] = apellido1

            elif not empleado.get('apellido2'):
                apellido2 = input('Ingresa el segundo apellido del empleado => ')
                if re.match(r'^[A-Za-z]+$', apellido2):
                    empleado['apellido2'] = apellido2

            elif not empleado.get('extension'):
                extension = input('Ingresa la extensión del empleado => ')
                if re.match(r'^[0-9]+$', extension):
                    empleado['extension'] = extension
            
            elif not empleado.get('email'):
                email = input('Ingresa el email del empleado => ')
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$', email):
                    empleado['email'] = email

            elif not empleado.get('codigo_oficina'):
                codigo_oficina = input('Ingresa el código de oficina del empleado => ')
                if re.match(r'^[0-9]{2,3}-[0-9]{2,3}$', codigo_oficina):
                    empleado['codigo_oficina'] = codigo_oficina

            elif not empleado.get('codigo_jefe'):
                codigo_jefe = input('Ingresa el código del jefe del empleado => ')
                if codigo_jefe.isdigit():
                    codigo_jefe = int(codigo_jefe)
                    empleado['codigo_jefe'] = codigo_jefe

            elif not empleado.get('puesto'):
                puesto = input('Ingresa el puesto del empleado => ')
                if re.match(r'^[A-Za-z\s]+$', puesto):
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

def updateEmpleado(id):
    data = gE.geAllId(id)
    if len(data):
        print("""
                  ¿Qué dato deseas actualizar?

              1. Código del empleado
              2. Nombre del empleado
              3. Primer apellido del empleado
              4. Segundo apellido del empleado
              5. Extensión del empleado
              6. Email del empleado
              7. Código de la oficina del empleado
              8. Código del jefe del empleado
              9. Puesto del cliente

       Presiona (Ctrl + C) para regresar al menú principal
              
 """)
    
    opcion = int(input('\nSeleccione una opción => '))
    for val in data:
        if opcion == 1:
            codigo = input('Ingresa el código del empleado => ')
            if codigo.isdigit():
                codigo = int(codigo)
                data = data[0]
                data['codigo_empleado'] = codigo

        if opcion == 2:
            nombre = input('Ingrese el nombre del empleado => ')
            if re.match(r'^[A-Za-z]+$', nombre):
                datamod = data[0]
                datamod['nombre'] = nombre

        if opcion == 3:        
            apellido1 = input('Ingresa el primer apellido del empleado => ')
            if re.match(r'^[A-Za-z]+$', apellido1):
                data = data[0]
                data['apellido1'] = apellido1          

        if opcion == 4:
            apellido2 = input('Ingresa el segundo apellido del empleado => ')
            if re.match(r'^[A-Za-z]+$', apellido2):
                data = data[0]
                data['apellido2'] = apellido2

        if opcion == 5:
            extension = input('Ingresa la extensión del empleado => ')
            if re.match(r'^[0-9]+$', extension):
                data = data[0]
                data['extension'] = extension
                
                
        if opcion == 6:
            email = input('Ingresa el email del empleado => ')
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$', email):
                    data = data[0]
                    data['email'] = email

        if opcion == 7:
            codigo_oficina = input('Ingresa la codigo de oficina del empleado => ')
            if re.match(r'^[0-9]{2,3}-[0-9]{2,3}$', codigo_oficina):
                    data = data[0]
                    data['codigo_oficina'] = codigo_oficina

        if opcion == 8:
            codigo_jefe = input('Ingresa el código del jefe del empleado => ')
            if codigo_jefe.isdigit():
                    data = data[0]
                    codigo_jefe = int(codigo_jefe)
                    data['codigo_jefe'] = codigo_jefe

        if opcion == 9:
            puesto = input('Ingresa el puesto del empleado => ')
            if re.match(r'^[A-Za-z\s]+$', puesto):
                data = data[0]
                data['puesto'] = puesto
            
            else:
                print('No cumple con los estandares establecidos')

    peticion = requests.put(f"http://154.38.171.54:5003/empleados/{id}", data=json.dumps(data[0]).encode("UTF-8"))
    res = peticion.json()
    return [res]


def menu():
    while True:
        os.system('clear')
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
                print(tabulate(postEmpleado(), headers='keys', tablefmt='fancy_grid'))
            if opcion == 2:
                id= input('Ingrese el Id del empleado que desee eliminar => ')
                print(tabulate(deleteEmpleado(id), headers='keys', tablefmt='fancy_grid')) # Aún asi funciona
            if opcion == 3:
                idE = input('Ingresa el ID del empleado que desee actualizar => ')
                print(tabulate(updateEmpleado(idE), headers='keys', tablefmt='fancy_grid'))
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break

        input('Presiona una la tecla Enter para continuar...')


