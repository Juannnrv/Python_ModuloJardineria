import requests
from tabulate import tabulate
import os

def getAllOficina():
   # http://154.38.171.54:5005/oficinas
   peticion = requests.get("http://154.38.171.54:5005/oficinas")
   data = peticion.json()
   return data

def getAllId(id):
   peticion = requests.get(f'http://154.38.171.54:5005/oficinas/{id}')
   if peticion.ok:
       return [peticion.json()]
   else:
       return []


def getOficinaCodigo(codigo):
   for val in getAllOficina():
      if(val.get('codigo_oficina')) == codigo:
         return [val]

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllOficina():
        codigoCiudad.append({
            'código': val.get('codigo_oficina'),
            'ciudad': val.get('ciudad')
        }) 
        
    return codigoCiudad



def getAllCiudadTelefonoEspaña():
    ciudadTelefono = []
    for val in getAllOficina():
        pais = val.get('pais')
        if pais == 'España':
            ciudadTelefono.append({

                'oficinas': val.get('codigo_oficina'),
                'ciudad': val.get('ciudad'),
                'telefono': val.get('telefono'),
                'pais': val.get('pais')
        }) 
        
    return ciudadTelefono 

def menu():
    os.system('clear')
    while True:

     print("""
           ---REPORTES DE LAS OFICINAS---
          
          1. Obtener código y ciudad de todas las oficinas
          2. Obtener ciudad y teléfono de las oficinas ubicadas en España
          
         Presiona (Ctrl + C) para regresar al menú principal
    """)
     try:
      opcion = int(input("\nSeleccione una de las opciones => "))
      if opcion == 1:
        print(tabulate(getAllCodigoCiudad(), headers='keys', tablefmt='fancy_grid'))
      elif opcion == 2:
        print(tabulate(getAllCiudadTelefonoEspaña(), headers='keys', tablefmt='fancy_grid'))
     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break
