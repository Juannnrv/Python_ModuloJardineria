import storage.pedido as ped
from datetime import datetime

def getAllEstadosPedidos():
    EstadosPedido = []

    for val in ped.pedido:
        EstadosPedido.append({

            'codigo_pedido': val.get('codigo_pedido'),
            'estado': val.get ('estado')

        })
    return EstadosPedido

def getAllPedidosAtrasadosDeTiempo():
    PedidosAceptados = []

    for val in ped.pedido:
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

    for val in ped.pedido:
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

    for val in ped.pedido:
        codigo_pedido = val.get('codigo_pedido')
        fecha_entrega = val.get('fecha_entrega')
        if fecha_entrega is not None and fecha_entrega.startswith("2009") and val.get('estado') == "Rechazado":
            PedidosRechazados2009.append({
                'codigo_pedido': codigo_pedido,
                'estado': val.get('estado'),
                'fecha_entrega': fecha_entrega
            })

    return PedidosRechazados2009
