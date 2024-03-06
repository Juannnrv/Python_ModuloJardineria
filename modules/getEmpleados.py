import storage.empleado as em 



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

def getAllNombrePuestoApellidoEmailJefe(codigo):
    nombrePuestoApellidoEmail = []
    
    for val in em.empleados:
        if (val.get ('codigo_jefe') == None):
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

            
