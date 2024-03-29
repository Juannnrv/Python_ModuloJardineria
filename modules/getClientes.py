import modules.getEmpleados as em 
import modules.getPagos as pago
import requests
import os

from tabulate import tabulate

def getAllCliente():
    peticion = requests.get('http://154.38.171.54:5001/cliente')
    data = peticion.json()
    return data

def getAllId(id):
    peticion = requests.get(f'http://154.38.171.54:5001/cliente/{id}')
    if peticion.ok:
        return [peticion.json()]
    else:
        return []

def getClienteCodigo(codigo):
   peticion = requests.get(f"http://154.38.171.54:5001/cliente/{codigo}") 

   return [peticion.json()] if peticion.ok else[]

def getAllClientsName():
    clienteName = []
    for val in getAllCliente():
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    for val in getAllCliente():
        if val.get('codigo_cliente') == codigo:
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente') 
            }
    return None

    
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = []
    for val in getAllCliente():
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in getAllCliente():
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) and
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone

def getAllClientesEspañoles():
    ClientesEspañoles = []
    for val in getAllCliente():
        if(val.get('pais') == 'Spain'):
            ClientesEspañoles.append({

            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "nombre_contacto": val.get('nombre_contacto'),
            'ciudad': val.get ('ciudad'),
            'region': val.get('region'),
            "pais": val.get('pais')
            })
    return ClientesEspañoles

def getAllMadridClients():
   ClientesMadrid = []
   for val in getAllCliente():
      if (val.get('ciudad') == 'Madrid'):
         if (val.get('codigo_empleado_rep_ventas') == 30) or (val.get('codigo_empleado_rep_ventas') == 11):
          ClientesMadrid.append({

            "codigo del cliente": val.get('codigo_cliente'),
            "nombre del cliente": val.get('nombre_cliente'),
            'ciudad': val.get ('ciudad'),
            'codigo_empleado_rep_ventas': val.get('codigo_empleado_rep_ventas'),

         })

   return ClientesMadrid      

def getAllRepVentasNombreApellido():
    NombreApellidoRepVentasClientes = []
    for clientes in getAllCliente():
        for empleados in em.getAllEmpleados():
            if clientes.get('codigo_empleado_rep_ventas') == empleados.get('codigo_empleado'):
                if empleados.get('puesto') == 'Representante Ventas':
                    NombreApellidoRepVentasClientes.append({
                        'nombre_cliente': clientes.get('nombre_cliente'),
                        "nombre": empleados.get('nombre'),
                        'apellido1': empleados.get('apellido1'),
                        'puesto': empleados.get('puesto')
                    })
    return NombreApellidoRepVentasClientes

def getAllPagosClientesPagos():
   PagosClientes = []
   for clientes in getAllCliente():
        for pagos in pago.getAllPagos():
            for empleados in em.getAllEmpleados():
              if clientes.get ('codigo_cliente') == pagos.get('codigo_cliente'):
                 if clientes.get ('codigo_empleado_rep_ventas') == empleados.get('codigo_empleado'):
                    if empleados.get('puesto') == 'Representante Ventas':
                     PagosClientes.append({

                       "codigo del cliente": clientes.get('codigo_cliente'),
                       'nombre del cliente': clientes.get('nombre_cliente'),
                       'id transaccion del pago': pagos.get('id_transaccion'),
                       'puesto': empleados.get('puesto'),
                       'nombre representante de ventas': empleados.get('nombre')
                    })
   return PagosClientes
                  
def getAllClientesNoPagos():
    ClientesNoPagos = []
    for clientes in getAllCliente():
        tiene_pagos = False
        for pagos in pago.getAllPagos():
            if clientes.get('codigo_cliente') == pagos.get('codigo_cliente'):
                tiene_pagos = True
                break
        if not tiene_pagos:
            for empleados in em.getAllEmpleados():
                if clientes.get('codigo_empleado_rep_ventas') == empleados.get('codigo_empleado'):
                    if empleados.get('puesto') == 'Representante Ventas':
                        ClientesNoPagos.append({

                            "codigo del cliente": clientes.get('codigo_cliente'),
                            'nombre del cliente': clientes.get('nombre_cliente'),
                            'puesto': empleados.get('puesto'),
                            'nombre representante de ventas': empleados.get('nombre')
                        })
    return ClientesNoPagos


def menu():
    
    while True:
        os.system('clear')
        print("""
        ---REPORTES DE LOS CLIENTES---
          
          1. Obtener todos los clientes (código y nombre)
          2. Obtener un cliente por su código (código y nombre)
          3. Obtener información detallada de un cliente por límite de crédito y ciudad
          4. Obtener información de todos los clientes españoles
          5. Obtener información de todos los clientes de la ciudad de Madrid cuyo representante de ventas tenga el código de empleado 11 o 30
          6. Obtener nombre y apellidos del representante de ventas de todos los clientes
          7. Obtener nombre de los clientes junto sus representantes de ventas que hayan hecho pagos 
          8. Obtener el nombre de todos los clientes junto sus representantes de ventas que no hayan realizado pagos  
             
       Presiona (Ctrl + C) para regresar al menú principal
        """)
        try:
            opcion = int(input("\nSeleccione una de las opciones => "))
            if opcion == 1:
                print(tabulate(getAllClientsName(), headers="keys", tablefmt="fancy_grid"))
            elif opcion == 2:
                codigo = int(input("Ingrese el código del cliente => "))
                cliente = getOneClientCodigo(codigo)
                if cliente:
                    print(tabulate([cliente], headers="keys", tablefmt="fancy_grid"))
            elif opcion == 3:
                limite = float(input("Ingrese el limite de credito de los clientes que desea visualizar => "))
                ciudad = input("Ingrese su limite crediticio y el nombre de la ciudad que desea filtrar => ")
                print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers="keys", tablefmt="fancy_grid"))
            elif opcion == 4:
                print(tabulate(getAllClientesEspañoles(), headers='keys', tablefmt='fancy_grid'))
            elif opcion == 5:
                print(tabulate(getAllMadridClients(), headers='keys', tablefmt='fancy_grid'))
            elif opcion == 6:
                print(tabulate(getAllRepVentasNombreApellido(), headers='keys', tablefmt='fancy_grid'))
            elif opcion == 7:
                print(tabulate(getAllPagosClientesPagos(), headers='keys', tablefmt='fancy_grid'))
            elif opcion == 8:
                print(tabulate(getAllClientesNoPagos(), headers='keys', tablefmt='fancy_grid'))      

            continuar = input("\n¿Desea continuar? Presione Enter.")
        except KeyboardInterrupt:
            print()
            print('SALIENDO...')
            break
