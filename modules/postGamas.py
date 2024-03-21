import json
import requests
import os
import re
import modules.getGamas as gG
from tabulate import tabulate

def postGama():
    # http://154.38.171.54:5004/gama
    gama = dict()
    while True:
        try:
            gamas = input('Ingrese la gama => ')
            if re.match(r'^[A-Za-z]+$', gamas):
                gama['gama'] = gamas

            descripcion_texto = input('Ingrese la descripción en texto => ')
            if(re.match(r'^[^\n]+$', descripcion_texto)):
                gama['descripcion_texto'] = descripcion_texto

            descripcion_html = input('Ingrese la descripción en html => ')
            if(re.match(r'^[^\n]+$', descripcion_html)):
                gama['descripcion_html'] = descripcion_html

            imagen = input('Ingrese la imagen => ')
            if(re.match(r'^[^\n]+$', imagen)):
                gama['imagen'] = imagen
            break

        except Exception as error:
            print('---ERROR---')
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post('http://154.38.171.54:5004/gama', headers=headers, data=json.dumps(gama)) 
    res = peticion.json()
    res ['Mensaje'] = 'Gama guardado'
    return [res]

def deleteGama(id):
    peticion = requests.delete(f'http://154.38.171.54:5004/gama/{id}')
    if peticion.status_code == 200:
        print('\nGama eliminada satisfactoriamente')

def updateGama(id):
    data = gG.getAllId(id)
    if len(data):
        print("""
                  ¿Qué dato deseas actualizar?

              1. Gama
              2. Descripción de la gama en texto
              3. Descripción de la gama en html
              4. Imagen de la gama
              
         Presiona (Ctrl + C) para regresar al menú principal
 """)
        opcion = int(input('Ingresa la opción => '))
        for val in data:

            if opcion == 1:
                gamas = input('Ingrese la gama => ')
                if re.match(r'^[A-Za-z]+$', gamas):
                    data = data[0]
                    data['gama'] = gamas

            elif opcion == 2:
                descripcion_texto = input('Ingrese la descripción en texto => ')
                if(re.match(r'^[^\n]+$', descripcion_texto)):
                    data = data[0]
                    data['descripcion_texto'] = descripcion_texto

            elif opcion == 3:
                descripcion_html = input('Ingrese la descripción en html => ')
                if(re.match(r'^[^\n]+$', descripcion_html)):
                    data = data[0]
                    data['descripcion_html'] = descripcion_html

            elif opcion == 4:
                imagen = input('Ingrese la imagen => ')
                if(re.match(r'^[^\n]+$', imagen)):
                    data = data[0]
                    data['imagen'] = imagen

            else:
                print('No cumple con los estandares establecidos')

    peticion = requests.put(f"http://154.38.171.54:5004/gama/{id}", data=json.dumps(data).encode("UTF-8"))
    res = peticion.json()
    return [res]



def menu():
    while True:
     os.system('clear')
     print("""
               ---ADMINISTRADOR DATOS DE GAMAS---
          
                    1. Guardar una gama nuevo
                    2. Eliminar un gama
                    3. Actualizar un gama existente
         
          Presiona (Ctrl + C) para regresar al menú principal
           
           """)
     try:
         opcion = int(input('\nSeleccione una de las opciones => '))
         if opcion == 1:
            print(tabulate(postGama(), headers='keys', tablefmt='fancy_grid'))
         elif opcion == 2:
             id = input('Ingrese el ID de la gama que desea eliminar => ')
             print(tabulate(deleteGama(id), headers='keys', tablefmt='fancy_grid'))
         elif opcion == 3:
             id = input('Ingrese el ID de la gama que desea actualizar => ')
             print(tabulate(updateGama(id), headers='keys', tablefmt='fancy_grid'))

     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break
     
     input('Presione la tecla Enter para poder continuar...')