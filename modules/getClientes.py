import storage.cliente as cli

from tabulate import tabulate

def getAllClientsName():
    clienteName = []
    for val in cli.clientes:
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if val.get('codigo_cliente') == codigo:
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente') 
            }
    return None

    
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = []
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in cli.clientes:
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) and
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone

def getAllClientesEspañoles():
    ClientesEspañoles = []
    for val in cli.clientes:
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

def menu():
    while True:

     print("""
        ---REPORTES DE LOS CLIENTES---
          
          1. Obtener todos los clientes (código y nombre)
          2. Obtener un cliente por su código (código y nombre)
          3. Obtener información detallada de un cliente por límite de crédito y ciudad
          4. Obtener información de todos los clientes españoles
          0. Regresar al menú principal
    """)
     opcion = int(input("\nSeleccione una de las opciones => "))
     if opcion == 1:
        print(tabulate(getAllClientsName(), headers = "keys", tablefmt= "fancy_grid"))
     elif opcion == 2:
       codigo = int(input("Ingrese el código del cliente => "))
       cliente = getOneClientCodigo(codigo)
       if cliente:
          print(tabulate([cliente], headers="keys", tablefmt="fancy_grid"))
     elif opcion == 3:
        limite = float(input("Ingrese el limite de credito de los clientes que desea visualizar => "))
        ciudad = input("Ingrese su limite crediticio y el nombre de la ciudad que desea filtrar => ")
        print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers = "keys", tablefmt= "fancy_grid"))
     elif opcion == 4:
        print(tabulate(getAllClientesEspañoles(), headers = 'keys', tablefmt = 'fancy_grid'))
     elif opcion == 0:
         print()
         break
