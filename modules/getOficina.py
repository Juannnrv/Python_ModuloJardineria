import requests
from tabulate import tabulate
import os

def getAllDataOficina():
   #json-server storage/oficina.json -b 5007
   peticion = requests.get("http://172.16.100.116:5504")
   data = peticion.json()
   return data

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllDataOficina():
        codigoCiudad.append({
            'código': val.get('codigo_oficina'),
            'ciudad': val.get('ciudad')
        }) 
        
    return codigoCiudad



def getAllCiudadTelefonoEspaña():
    ciudadTelefono = []
    for val in getAllDataOficina():
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
