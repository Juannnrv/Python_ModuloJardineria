import storage.pedido as ped

def getAllEstadosPedidos():
    EstadosPedido = []

    for val in ped.pedido:
        EstadosPedido.append({

            'codigo_pedido': val.get('codigo_pedido'),
            'estado': val.get ('estado')

        })
    return EstadosPedido