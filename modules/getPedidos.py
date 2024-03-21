from datetime import datetime
from tabulate import tabulate
import requests


def getAllPedidos():
    # http://154.38.171.54:5007/pedidos
   peticion = requests.get('http://154.38.171.54:5007/pedidos')
   data = peticion.json()
   return data

def getAllId(id):
    peticion = requests.get(f'http://154.38.171.54:5007/pedidos/{id}')
    if peticion.ok:
        return [peticion.json()]
    else:
        return []
    
def getAllCodigo(codigo):
    for val in getAllPedidos():
       if(val.get('codigo_pedido')) == codigo:
          return [val]
    return []


def getAllEstadosPedidos():
    EstadosRepetidos = set()
    EstadosPedido = []

    for val in getAllPedidos():
        if val.get('estado') not in EstadosRepetidos:   
         EstadosPedido.append({

            
            'estado': val.get ('estado')

        })
        EstadosRepetidos.add(val.get('estado'))
    return EstadosPedido

def getAllPedidosAtrasadosDeTiempo():
    PedidosAceptados = []

    for val in getAllPedidos():
        if (val.get('estado') == 'Entregado') and val.get('fecha_entrega') is None:
            val['fecha_entrega'] = val.get('fecha_esperada')
        if val.get('estado') == 'Entregado':
            date_1 = '/'.join(val.get('fecha_esperada').split('-')[::-1])
            date_2 = '/'.join(val.get('fecha_entrega').split('-')[::-1])
            start = datetime.strptime(date_1, '%d/%m/%Y')
            end = datetime.strptime(date_2, '%d/%m/%Y')
            diff = end.date() - start.date()
            if diff.days < 0:
                PedidosAceptados.append({

                    'codigo_pedido': val.get('codigo_pedido'),
                    'codigo_cliente': val.get('codigo_cliente'),
                    'fecha_esperada': val.get('fecha_esperada'),
                    'fecha_entrega': val.get('fecha_entrega')

                })

    return PedidosAceptados

def getAllPedidosEntregados2DiasAntes():
    PedidosEntregados2DiasAntes = []

    for val in getAllPedidos():
        if (val.get('estado') == 'Entregado') and val.get('fecha_entrega') is None:
            val['fecha_entrega'] = val.get('fecha_esperada')
        
        if val.get('estado') == 'Entregado':
            date_1 = '/'.join(val.get('fecha_esperada').split('-')[::-1])
            date_2 = '/'.join(val.get('fecha_entrega').split('-')[::-1])
            start = datetime.strptime(date_1, '%d/%m/%Y')
            end = datetime.strptime(date_2, '%d/%m/%Y')
            diff = (end.date() - start.date()).days
            if diff < -1: 
                PedidosEntregados2DiasAntes.append({
                    'codigo_pedido': val.get('codigo_pedido'),
                    'codigo_cliente': val.get('codigo_cliente'),
                    'fecha_esperada': val.get('fecha_esperada'),
                    'fecha_entrega': val.get('fecha_entrega')
                })

    return PedidosEntregados2DiasAntes
        
def getAllPedidosRechazados2009():
    PedidosRechazados2009 = []

    for val in getAllPedidos():
        codigo_pedido = val.get('codigo_pedido')
        fecha_entrega = val.get('fecha_entrega')
        if fecha_entrega is not None and fecha_entrega.startswith("2009") and val.get('estado') == "Rechazado":
            PedidosRechazados2009.append({
                'codigo_pedido': codigo_pedido,
                'estado': val.get('estado'),
                'fecha_entrega': fecha_entrega
            })

    return PedidosRechazados2009

def getPedidosEntregadosEnEnero():
    pedidos_entregados_en_enero = []

    for pedido in getAllPedidos():
        fecha_entrega = pedido.get('fecha_entrega')
        if fecha_entrega is not None:
            fecha_entrega_dt = datetime.strptime(fecha_entrega, '%Y-%m-%d')
            if fecha_entrega_dt.month == 1 and pedido.get('estado') == 'Entregado': 
                pedidos_entregados_en_enero.append({
                    'codigo_pedido': pedido.get('codigo_pedido'),
                    'fecha_entrega': fecha_entrega,
                    'estado': pedido.get('estado')
                })

    return pedidos_entregados_en_enero

def menu():
    while True:
     print("""
        ---REPORTES DE LOS PEDIDOS---
          
          1. Obtener todos los estados por los que puede pasar un pedido
          2. Obtener Codigo de los clientes los cuales no les fue entregado el pedido a tiempo junto sus fechas de espera y entrega
          3. Obtener Codigo de los clientes los cuales les fue entregado el pedido a tiempo con al menos 2 dias de anterioridad
          4. Obtener todos los pedidos que fueron rechazados en 2009
          5. Obtener todos los pedidos que fueron entregados en Enero
          
       Presiona (Ctrl + C) para regresar al menú principal
    
""")
     try:
         
      opcion = int(input("\nSeleccione una de las opciones => "))
      if opcion == 1:
         print(tabulate(getAllEstadosPedidos(), headers = "keys", tablefmt= "fancy_grid"))
      elif opcion == 2:
        print(tabulate(getAllPedidosAtrasadosDeTiempo(), headers = "keys", tablefmt= "fancy_grid"))
      elif opcion == 3:
        print(tabulate(getAllPedidosEntregados2DiasAntes(), headers = "keys", tablefmt= "fancy_grid"))
      elif opcion == 4:
        print(tabulate(getAllPedidosRechazados2009(), headers = "keys", tablefmt= "fancy_grid"))
      elif opcion == 5:
        print(tabulate(getPedidosEntregadosEnEnero(), headers = "keys", tablefmt= "fancy_grid"))
     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break
