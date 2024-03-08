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

def getAllCodigoClientes(codigo):
    for val in cli.clientes:
        if val.get('codigo_cliente') == codigo:
            return{
               "codigo_cliente": val.get('codigo_cliente'),
               "nombre_cliente": val.get('nombre_cliente') 
            }
    
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

def getAllClientesEspañoles(pais):
    ClientesEspañoles = []
    for val in cli.clientes:
        if(val.get('pais') == 'Spain'):
            ClientesEspañoles.append({

            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "nombre_contacto": val.get('nombre_contacto'),
            "pais": val.get('pais')
            })
    return ClientesEspañoles

def menu():
    print("""
        REPORTES DE LOS CLIENTES
          
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la informción de un cliente según su límite de crédito y ciudad que pertenece (ejem: 3000.0, San Francisco)
""")
    opcion = int(input("\nSeleccione una de las opciones => "))
    if opcion == 1:
        print(tabulate(getAllClientsName(), headers = "keys", tablefmt= "rounded_grid"))
    elif opcion == 2:
        codigo = input("Ingrese el código del cliente => ")
        print(tabulate(getAllCodigoClientes(codigo), headers = "keys", tablefmt= "rounded_grid"))
    elif opcion == 3:
        limite = float(input("Ingrese el limite de credito de los clientes que desea visualizar: "))
        ciudad = input("Ingrese su limite crediticio y el nombre de la ciudad que desea filtrar => ")
        print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers = "keys", tablefmt= "rounded_grid"))
