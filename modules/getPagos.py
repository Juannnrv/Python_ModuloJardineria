import storage.pago as pago
from datetime import datetime

def getAllPagos2008():
    codigos_clientes_vistos = set() 
    pagos_2008 = []

    for val in pago.pago:
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

    for val in pago.pago:
        fecha_pago = val.get('fecha_pago')
        forma_pago = val.get('forma_pago')
        if fecha_pago is not None:
            fecha_pago_dt = datetime.strptime(fecha_pago, '%Y-%m-%d')
            if fecha_pago_dt.year == 2008 and forma_pago == 'Paypal':
                pedidos2008Paypal.append({

                    'codigo_cliente': val.get('codigo_cliente'),
                    'forma_pago': val.get ('forma_pago'),
                    'fecha_pago': val.get ('fecha_pago')
                })
    pedidos2008Paypal.sort(key=lambda x: x['fecha_pago'])


    return pedidos2008Paypal
