from datetime import datetime
import requests
from tabulate import tabulate


def getAllPagos():
   Pagos = []
   peticion = requests.get('http://154.38.171.54:5006/pagos')
   data = peticion.json()
   return data

def getAllId(id):
   peticion = requests.get(f'http://154.38.171.54:5006/pagos/{id}')
   if peticion.ok:
      return [peticion.json()]
   else:
      return []
   
def getAllClientsCodigo(codigo_cliente):
   for val in getAllPagos():
      if (val.get('codigo_cliente') == codigo_cliente):
         return [val]


def getAllClientesPagos2008():
    codigos_clientes_vistos = set() 
    pagos_2008 = []

    for val in getAllPagos():
        codigo_cliente = val.get('codigo_cliente')
        if val.get('fecha_pago').startswith('2008') and codigo_cliente not in codigos_clientes_vistos:
            pagos_2008.append({
                'codigo_cliente': codigo_cliente,
                'total': val.get('total'),
                'fecha_pago': val.get('fecha_pago')
            })
            codigos_clientes_vistos.add(codigo_cliente)  

    return pagos_2008


def getAllPedidos2008ConPaypal():
    pedidos2008Paypal = []

    for val in getAllPagos():
        fecha_pago = val.get('fecha_pago')
        forma_pago = val.get('forma_pago')
        if fecha_pago is not None:
            fecha_pago_dt = datetime.strptime(fecha_pago, '%Y-%m-%d')
            if fecha_pago_dt.year == 2008 and forma_pago == 'PayPal':
                pedidos2008Paypal.append({

                    'codigo_cliente': val.get('codigo_cliente'),
                    'forma_pago': val.get ('forma_pago'),
                    'fecha_pago': val.get ('fecha_pago')
                })
    pedidos2008Paypal.sort(key=lambda x: x['fecha_pago'])


    return pedidos2008Paypal


def getAllFormasDePago():
    FormasDePagoRepetidas = set()
    FormasDePago = []

    for val in getAllPagos():
        forma_pago = val.get ('forma_pago')
        if (val.get ('forma_pago')) is not None and forma_pago not in FormasDePagoRepetidas:
            FormasDePago.append({

                'forma_pago': val.get ('forma_pago')
            })

            FormasDePagoRepetidas.add(forma_pago)

    return FormasDePago
            
def menu():
    while True:

     print("""
        ---REPORTES DE LOS PAGOS---
          
          1. Obtener todos los codigos de clientes que han realizado pagos en 2008
          2. Obtener todos los pagos realizados mediante Paypal en 2008
          3. Obtener toda las formas de pago
          
       Presiona (Ctrl + C) para regresar al menú principal
""")
     try:
         
      opcion = int(input("\nSeleccione una de las opciones => "))
      if opcion == 1:
        print(tabulate(getAllClientesPagos2008(), headers = "keys", tablefmt= "fancy_grid"))
      elif opcion == 2:
         print(tabulate(getAllPedidos2008ConPaypal(), headers = "keys", tablefmt= "fancy_grid")) 
      elif opcion == 3:
         print(tabulate(getAllFormasDePago(), headers = "keys", tablefmt= "fancy_grid")) 
     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break