from tabulate import tabulate

import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedidos as pedido
import modules.getPagos as pagos
import modules.getProducto as producto 

if __name__ == "__main__":
    while True:
        print(''' 
                    ---MENÚ PRINCIPAL---
            
                        1. Clientes
                        2. Oficinas
                        3. Empleados
                        4. Pedidos
                        5. Pagos
                        6. Productos
              
                 Presiona (Ctrl + C) para Salir
''')
        try:
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
            elif opcion == 6:
                producto.menu()
        except KeyboardInterrupt:
              print('SALIENDO...')
              break

     