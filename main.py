import os
import re
from tabulate import tabulate


import modules.getClientes as Repclientes
import modules.postClientes as CRUDclientes
from modules import postClientes

import modules.getOficina as Repoficina
import modules.postOficinas as CRUDoficina
from modules import postOficinas

import modules.getEmpleados as Repempleado
import modules.postEmpleados as CRUDempleados
from modules import postEmpleados
import modules.getPedidos as pedido
import modules.getPagos as pagos
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto
from modules import postProducto

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
           opcion = int(input("\nSelecione una de las opciones => "))
           if(re.match(r'[0-9]+$', opcion) is not None):
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
        opcion = int(input('\nSelecciones una de las opciones => '))
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
            opcion = int(input('\nSeleccione una de las opciones => '))
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
           opcion = int(input("\nSelecione una de las opciones: "))
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
            
            
if __name__ == "__main__":
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
              
                 Presiona (Ctrl + C) para Salir
''')
        try:
            opcion = int(input('\n Seleccione una de las opciones => '))
            if(re.match(r'[0-9]+$', opcion) is not None):
                 opcion = int(opcion)
                 if (opcion>=0 and opcion<=5):
                    if opcion == 1:
                        menuClientes()
                    elif opcion == 2:
                        menuOficina()
                    elif opcion == 3:
                        menuEmpleados()
                    elif opcion == 4: 
                        pedido.menu()
                    elif opcion == 5:
                        pagos.menu()
                    elif opcion == 6:
                        menuProducto()
        except KeyboardInterrupt:
            print('SALIENDO...')
            break

     