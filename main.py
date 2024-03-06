from tabulate import tabulate

import modules.getClientes as clientes

import modules.getOficina as oficina 

print(tabulate(oficina.getAllCiudadTelefono('EEUU'), tablefmt = 'grid'))
