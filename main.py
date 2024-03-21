import os
import re
import json
import requests
from tabulate import tabulate


import modules.getClientes as Repclientes
import modules.postClientes as CRUDclientes

import modules.getOficina as Repoficina
import modules.postOficinas as CRUDoficina

import modules.getEmpleados as Repempleado
import modules.postEmpleados as CRUDempleados

import modules.getPedidos as pedido

import modules.getPagos as Reppagos
import modules.postPagos as CRUDpagos

import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto

import modules.getGamas as Repgamas
import modules.postGamas as CRUDgama

import modules.getDetallePedido as Repdetallepedido
import modules.postDetallePedido as CRUDdetallepedido


def menuClientes():
    while True:
        os.system('clear')
        print('''
                    ---BIENVENIDO AL MENÚ DE CLIENTES---

                1. Reportes de los clientes
                2. Guardar, Actualizar y Eliminar clientes

                        Presiona (Ctrl + C) para Salir
        ''')
        try:
           opcion = (input("\nSelecione una de las opciones => "))
           if(re.match(r'\d+', opcion) is not None):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=2):
                    if(opcion == 1):
                        Repclientes.menu()
                    elif(opcion == 2):
                        CRUDclientes.menu()
        except KeyboardInterrupt:
              print('SALIENDO...')
              break

def menuOficina():
    while True:
     os.system('clear')
     print("""
                    ---BIENVENIDO AL MENÚ DE OFICINAS---

                1. Reportes de las oficinas
                2. Guardar, Actualizar y Eliminar oficina

                        Presiona (Ctrl + C) para Salir

""")
     try:
        opcion = (input('\nSelecciones una de las opciones => '))
        if(re.match(r'[0-9]+$', opcion) is not None):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=2):
                    if opcion == 1:
                        Repoficina.menu()
                    elif opcion == 2:
                        CRUDoficina.menu()
     except KeyboardInterrupt:
        print()
        print()
        print('SALIENDO...')
        break


def menuEmpleados():
    while True:
        os.system('clear')
        print("""
                    ---BIENVENIDO AL MENÚ DE EMPLEADOS---

                1. Reportes de los empleados
                2. Guardar, Actualizar y Eliminar empleados

                        Presiona (Ctrl + C) para Salir

""")
        try:
            opcion = (input('\nSeleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=2):
                    if opcion == 1:
                        Repempleado.menu()
                    elif opcion == 2:
                        CRUDempleados.menu()
        except KeyboardInterrupt:
            print()
            print()
            print('SALIENDO...')
            break

def menuPago():
    while True:
        os.system('clear')
        print('''
                    ---BIENVENIDO AL MENÚ DE PAGOS---

                1. Reportes de los pagos
                2. Guardar, Actualizar y Eliminar pagos

                        Presiona (Ctrl + C) para Salir
        ''')
        try:
           opcion = (input("\nSelecione una de las opciones: "))
           if(re.match(r'[0-9]+$', opcion) is not None):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=2):
                    if(opcion == 1):
                        Reppagos.menu()
                    elif(opcion == 2):
                        CRUDpagos.menu()
        except KeyboardInterrupt:
              print('SALIENDO...')
              break

def menuProducto():
    while True:
        os.system('clear')
        print('''
                    ---BIENVENIDO AL MENÚ DE PRODUCTOS---

                1. Reportes de los productos
                2. Guardar, Actualizar y Eliminar productos

                        Presiona (Ctrl + C) para Salir
        ''')
        try:
           opcion = (input("\nSelecione una de las opciones: "))
           if(re.match(r'[0-9]+$', opcion) is not None):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=2):
                    if(opcion == 1):
                        Repproducto.menu()
                    elif(opcion == 2):
                        CRUDproducto.menu()
        except KeyboardInterrupt:
              print('SALIENDO...')
              break
        
def menuGama():
    while True:
        os.system('clear')
        print('''
                    ---BIENVENIDO AL MENÚ DE GAMAS---

                1. Guardar, Actualizar y Eliminar gamas

                        Presiona (Ctrl + C) para Salir
        ''')
        try:
           opcion = (input("\nSelecione una de las opciones: "))
           if(re.match(r'[0-9]+$', opcion)):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=1):
                    if(opcion == 1):
                        CRUDgama.menu()
        except KeyboardInterrupt:
              print('SALIENDO...')
              break
        
def menuDetallepedido():
    while True:
        os.system('clear')
        print('''
                    ---BIENVENIDO AL MENÚ DE DETALLES DE PEDIDO---

                1. Guardar, Actualizar y Eliminar detalles de pedido

                           Presiona (Ctrl + C) para Salir
        ''')
        try:
           opcion = (input("\nSelecione una de las opciones: "))
           if(re.match(r'[0-9]+$', opcion)):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=1):
                    if(opcion == 1):
                        CRUDdetallepedido.menu()
        except KeyboardInterrupt:
              print('SALIENDO...')
              break


if __name__ == "__main__":

    #peticion = requests.get('http://154.38.171.54:5008/productos?gama=Ornamentales&cantidadEnStock_gte=100&_sort=-precio_venta')
    #data = json.dumps(peticion.json(), indent=4)
    #print(data)


    #with open('storage/producto.json', 'r') as f:
    #    fichero = f.read()
    #    data = json.loads(fichero)
    #    for i,val in enumerate(data):
    #        data[i]['id'] = (i+1)
    #    print(data)
    #    f.close()

    while True:
        os.system('clear')
        print('''
                    ---MENÚ PRINCIPAL---

                        1. Clientes
                        2. Oficinas
                        3. Empleados
                        4. Pedidos
                        5. Pagos
                        6. Productos
                        7. Gama
                        8. Detalle de pedido

                 Presiona (Ctrl + C) para Salir
''')
        opcion = (input('\n Seleccione una de las opciones => '))
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion>=0 and opcion<=8):
                    if opcion == 1:
                        menuClientes()
                    elif opcion == 2:
                        menuOficina()
                    elif opcion == 3:
                        menuEmpleados()
                    elif opcion == 4:
                        pedido.menu()
                    elif opcion == 5:
                        menuPago()
                    elif opcion == 6:
                        menuProducto()
                    elif opcion == 7:
                        menuGama()
                    elif opcion == 8:
                        menuDetallepedido()
                    elif opcion == 0:
                        break
                    print('SALIENDO...')


