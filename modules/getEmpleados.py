from tabulate import tabulate
import requests

def getAllDataEmpleados():
   #json-server storage/empleado.json -b 5006
   peticion = requests.get('http://172.16.106.67:5006')
   data = peticion.json()
   return data

def getAllNombreApellidoEmailJefe():
    nombreApellidoEmail = []
    
    for val in getAllDataEmpleados():
        if (val.get('codigo_jefe') == None):
            nombreApellidoEmail.append(
            {
                'nombre': val.get('nombre'),
                'apellidos': f'{val.get("apellido1")} {val.get("apellido2")}',
                'email': val.get('email'),
                'puesto': val.get('puesto'),
            }
        )
    return nombreApellidoEmail

def getAllNombrePuestoApellidoEmailJefe():
    nombrePuestoApellidoEmail = []
    
    for val in getAllDataEmpleados():
        if ( val.get ('codigo_jefe') == 7):
            nombrePuestoApellidoEmail.append({

                'nombre': val.get('nombre'),
                'apellidos': f'{val.get("apellido1")} {val.get("apellido2")}',
                'email': val.get('email'),
                'puesto': val.get ('puesto'),
                'jefe': val.get('codigo_jefe'),
            }
            )
    return nombrePuestoApellidoEmail

def getAllNombreApellidosPuestoNoRepresentantesDeVentas():
    nombreApellidosPuestoNoRepresentantesDeVentas = []

    for val in getAllDataEmpleados():
        if (val.get ('puesto') != 'Representante Ventas'):
            nombreApellidosPuestoNoRepresentantesDeVentas.append({

                'nombre': val.get('nombre'),
                'apellidos': f'{val.get("apellido1")} {val.get("apellido2")}',
                'email': val.get('email'),
                'puesto': val.get ('puesto')
            }
            )
    return nombreApellidosPuestoNoRepresentantesDeVentas


def menu():
    while True:

     print("""
        ---REPORTES DE LOS EMPLEADOS---
          
          1. Obtener nombres, apellidos y emails de los empleados cuyo jefe tiene un código igual a 7
          2. Obtener información sobre el jefe de la empresa
          3. Obtener información de los empleados que no son representantes de ventas
           
       Presiona (Ctrl + C) para regresar al menú principal
    """)
     try:
         
      opcion = int(input('Seleccione una de las opciones => '))
      if opcion == 1:
        print(tabulate(getAllNombrePuestoApellidoEmailJefe(), headers="keys", tablefmt="fancy_grid"))
      elif opcion == 2:
        print(tabulate(getAllNombreApellidoEmailJefe(), headers="keys", tablefmt="fancy_grid"))
      elif opcion == 3:
        print(tabulate(getAllNombreApellidosPuestoNoRepresentantesDeVentas(), headers="keys", tablefmt="fancy_grid"))
     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break

    