from tabulate import tabulate

import modules.getClientes as clientes

import modules.getOficina as oficina 

import modules.getEmpleados as empleado

import modules.getPedidos as pedido

print(tabulate(pedido.getAllEstadosPedidos(), tablefmt = 'grid'))
