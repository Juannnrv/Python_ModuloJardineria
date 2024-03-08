from tabulate import tabulate
import sys

import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedidos as pedido
import modules.getPagos as pagos

if(__name__ == "__main__"):
    print(''' 
  __  __              __    _____      _            _             _ 
 |  \/  |            /_/   |  __ \    (_)          (_)           | |
 | \  / | ___ _ __  _   _  | |__) | __ _ _ __   ___ _ _ __   __ _| |
 | |\/| |/ _ \ '_ \| | | | |  ___/ '__| | '_ \ / __| | '_ \ / _` | |
 | |  | |  __/ | | | |_| | | |   | |  | | | | | (__| | |_) | (_| | |
 |_|  |_|\___|_| |_|\__,_| |_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                     | |            
                                                     |_|       
                        1. Clientes
                        2. Oficinas
                        3. Empleados
                        4. Pedidos
                        5. Pagos
          
''')
    opcion = int(input('\n Seleccione una de las opciones => '))
    if opcion == 1:
        clientes.menu()
    elif opcion == 2:
        oficina.menu()
    elif opcion == 3:
        empleado.menu()
    elif opcion == 4: 
        pedido.menu()
    elif opcion == 5:
        pagos.menu()
    print()