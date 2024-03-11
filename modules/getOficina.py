import storage.oficina as of
from tabulate import tabulate


def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            'código': val.get('codigo_oficina'),
            'ciudad': val.get('ciudad')
        }) 
        
    return codigoCiudad



def getAllCiudadTelefonoEspaña():
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get('pais') == 'España'):
            ciudadTelefono.append({

                'oficinas': val.get('codigo_oficina'),
                'ciudad': val.get('ciudad'),
                'telefono': val.get('telefono'),
                'pais': val.get('pais')
        }) 
        
    return ciudadTelefono 

def menu():
    while True:

     print("""
           ---REPORTES DE LAS OFICINAS---
          
          1. Obtener código y ciudad de todas las oficinas
          2. Obtener ciudad y teléfono de las oficinas ubicadas en España
          0. Regresar al menú principal
    """)

     opcion = int(input("\nSeleccione una de las opciones => "))
     if opcion == 1:
        print(tabulate(getAllCodigoCiudad(), headers='keys', tablefmt='fancy_grid'))
     elif opcion == 2:
        print(tabulate(getAllCiudadTelefonoEspaña(), headers='keys', tablefmt='fancy_grid'))
     elif opcion == 0:
         print()
         break
