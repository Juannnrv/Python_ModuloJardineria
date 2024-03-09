import storage.empleado as em 
from tabulate import tabulate


def getAllNombreApellidoEmailJefe():
    nombreApellidoEmail = []
    
    for val in em.empleados:
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
    
    for val in em.empleados:
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

    for val in em.empleados:
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
    print("""
        ---REPORTES DE LOS EMPLEADOS---
          
          1. Obtener todos los nombres, apellidos y emails de los empleados cuyo jefe tine un codigo igual a 7
          2. Obtener información acerca del jefe de la empresa
          3. Obtener información de los empleados que no son representantes de ventas
""")

    opcion = int(input('\n Seleccione una de las opciones => '))
    if opcion == 1:
     print(tabulate(getAllNombrePuestoApellidoEmailJefe(), headers = "keys", tablefmt= "fancy_grid"))
    elif opcion == 2:
     print(tabulate(getAllNombreApellidoEmailJefe(), headers = "keys", tablefmt= "fancy_grid"))
    elif opcion == 3:
        print(tabulate(getAllNombreApellidosPuestoNoRepresentantesDeVentas(), headers = "keys", tablefmt= "fancy_grid"))
    