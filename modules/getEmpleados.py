import storage.empleado as em 
from tabulate import tabulate


def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    
    for val in em.empleados:
        if (val.get('codigo_jefe') == codigo):
            nombreApellidoEmail.append(
            {
                'nombre': val.get('nombre'),
                'apellidos': f'{val.get("apellido1")} {val.get("apellido2")}',
                'email': val.get('email'),
                'jefe': val.get('codigo_jefe'),
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

def getAllNombreApellidosPuestoNoRepresentantesDeVentas(codigo):
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
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la información de un cliente según su límite de crédito y ciudad que pertenece (ejem: 3000.0, San Francisco)
          4. Obtener información de todos los clientes españoles
""")

    opcion = int(input('\n Seleccione una de las opciones => '))
    if opcion == 1:
     print(tabulate(getAllNombrePuestoApellidoEmailJefe(), headers = "keys", tablefmt= "fancy_grid"))