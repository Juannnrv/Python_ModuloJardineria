from tabulate import tabulate

import modules.getClientes as clientes

import modules.getOficina as oficina 

import modules.getEmpleados as empleado

import modules.getPedidos as pedido

import modules.getPagos as pagos

print(tabulate(pedido.getAllPedidosRechazados2009(), tablefmt='grid'))
