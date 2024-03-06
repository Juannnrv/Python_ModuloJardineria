from tabulate import tabulate

import modules.getClientes as clientes

import modules.getOficina as oficina 

import modules.getEmpleados as empleado

print(tabulate(empleado.getAllNombrePuestoApellidoEmailJefe(1), tablefmt = 'grid'))
