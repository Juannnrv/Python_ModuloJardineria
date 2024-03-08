import storage.cliente as cli

from tabulate import tabulate

def getAllClientesName():
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
        if (val.get('codigo_cliente') == codigo):
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
  _____                       _                  _        _                  _ _            _            
 |  __ \                     | |                | |      | |                | (_)          | |           
 | |__) |___ _ __   ___  _ __| |_ ___  ___    __| | ___  | | ___  ___    ___| |_  ___ _ __ | |_ ___  ___ 
 |  _  // _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \ | |/ _ \/ __|  / __| | |/ _ \ '_ \| __/ _ \/ __|
 | | \ \  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | | (_) \__ \ | (__| | |  __/ | | | ||  __/\__ \
 |_|  \_\___| .__/ \___/|_|   \__\___||___/  \__,_|\___| |_|\___/|___/  \___|_|_|\___|_| |_|\__\___||___/
            | |                                                                                          
            |_|                                                                                          
          
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la informción de un cliente según su límite de crédito y ciudad que pertenece (ejem: 3000.0, San Francisco)
""")
    opcion = int(input('\n Seleccione una de las opciones => '))
    if (opcion == 1):
        print(tabulate(getAllClientesName(), headers = 'keys', tablefmt = 'github'))
    elif (opcion == 2):
        codigoCliente = int(input('\n Ingrese el código del cliente => '))
        print(tabulate(cli.getOneClientCodigo(codigoCliente), headers = 'keys', tablefmt = 'github')) 
