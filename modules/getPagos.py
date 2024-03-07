import storage.pago as pago

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


