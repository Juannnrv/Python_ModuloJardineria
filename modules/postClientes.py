import json
import requests
import os
import re
import modules.getClientes as gC
from tabulate import tabulate


def postClientes():
    #json-server storage/cliente.json -b 5503

    cliente = dict()
    while True:
        try:
           if(not cliente.get('codigo_cliente')):
              codigo = input('Ingrese el código del cliente => ')
              if str(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                data = gC.getAllClientsCodigo(codigo)
                if (data):
                     print(tabulate(data, headers='keys', tablefmt='fancy grid'))
                     raise Exception('El código no cumple con los estandares establecidos')
                else:
                    cliente['codigo_cliente'] = codigo
              else:
                  raise Exception("--> El código no cumple con el estándar establecido")

           if(not cliente.get('nombre_cliente')):
                nombre = input('Ingrese el nombre del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', nombre) is not None):
                    cliente['nombre_cliente'] = nombre

           if(not cliente.get('nombre_contacto')):
                nombre = input('Ingrese el nombre de contacto del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', nombre) is not None):
                    cliente['nombre_contacto'] = nombre  

           if(not cliente.get('apellido_contacto')):
                apellido = input('Ingrese el apellido de contacto del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', apellido) is not None):
                    cliente['apellido_contacto'] = apellido
                    
           if(not cliente.get('telefono')):
                telefono = input('Ingrese el telefono del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', telefono) is not None):
                    cliente['telefono'] = telefono
        
           if(not cliente.get('fax')):
                fax = input('Ingrese el fax del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', fax) is not None):
                    cliente['fax'] = fax     

           if(not cliente.get('linea_direccion1')):
                direccion_1 = input('Ingrese la diección 1 del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', direccion_1) is not None):
                    cliente['direccion_1'] = direccion_1    

           if(not cliente.get('linea_direccion2')):
                direccion_2 = input('Ingrese la diección 1 del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', direccion_2) is not None):
                    cliente['direccion_2'] = direccion_2

           if(not cliente.get('ciudad')):
                ciudad = input('Ingrese la diección 1 del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', ciudad) is not None):
                    cliente['ciudad'] = ciudad

           if(not cliente.get('region')):
                region = input('Ingrese la región del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', region) is not None):
                    cliente['region'] = region    

           if(not cliente.get('pais')):
                pais = input('Ingrese el país del cliente => ')
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', pais) is not None):
                    cliente['pais'] = pais     



                              
        
    cliente = {
        'codigo_producto': int(input('Ingrese el código del producto => ')),
        'nombre_cliente': input('Ingrese el nombre del cliente => '),
        'nombre_contacto': input('Ingrese el nombre del contacto => '),
        'apellido_contacto': input('Ingrese el apellido del contacto => '),
        'telefono': input('Ingrese el telefono => '),
        'fax': input('Ingrese el fax => '),
        'linea_direccion1': input('Ingrese la linea de direccion 1 => '),
        'linea_direccion2': input('Ingrese la linea de direccion 2 => '),
        'ciudad': input('Ingrese la ciudad => '),
        'region': input('Ingrese la region => '),
        'pais': input('Ingrese el pais => '),
        'codigo_postal': input('Ingrese el codigo postal => '),
        'codigo_empleado_rep_ventas': int(input('Ingresa el codigo del representante de ventas => ')),
        'limite_credito': int(input('Ingrese el limite crediticio => '))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://172.16.103.28:5503', headers=headers, data=json.dumps(cliente)) 
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