from tabulate import tabulate

import modules.getClientes as clientes

import modules.getOficina as oficina 

import modules.getEmpleados as empleados

print(tabulate(empleados.em.empleados('EEUU'), tablefmt = 'grid'))
