import json
import requests
import os
import re
import modules.getClientes as gC
from tabulate import tabulate

 #  Falta delete y put

def postClientes():
    # http://154.38.171.54:5001/cliente

    cliente = dict()
    while True:
        try:
           if(not cliente.get('codigo_cliente')):
                while True:
                    codigo = input('Ingrese el codigo del cliente => ')
                    if (codigo.isdigit()):
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
                    cliente['codigo_empleado_rep_ventas'] = codigo_empleado_rep_ventas

           if(not cliente.get('limite_credito')):
                limite_credito = input('Ingrese el límite crediticio del cliente => ')
                if re.match(r'^[0-9]+(\.[0-9]+)?$', limite_credito):
                    cliente['limite_credito'] = float(limite_credito)
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

def menu():
    while True:
     os.system('clear')
     print("""
               ---ADMINISTRADOR DATOS DE CLIENTES---
          
                    1. Guardar un cliente nuevo
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
        opcion = int(input('\nSeleccione una de las opciones => '))
        if opcion == 1:
           print(tabulate(postClientes(), headers='keys', tablefmt='fancy grid'))
     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break