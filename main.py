from tabulate import tabulate

import modules.getClientes as cliente 

print(tabulate(cliente.getAllClientPaisRegionCiudad('Spain', 'Fuenlabrada', 'Madrid'), tablefmt = 'grid'))
