import requests
from tabulate import tabulate
import modules.postProducto as psProducto

def getAllData():
   #json-server storage/producto.json -b 5502
   peticion = requests.get("http://172.16.100.116:5502")
   data = peticion.json()

   return data

def getAllStocksPriceGama():
    stockPriceGama = []
    for val in getAllData():
        gama = val.get('gama')
        stock = val.get('cantidad_en_stock')
        descripcion = val.get('descripcion')
        if gama == 'Ornamentales' and stock >= 100:
            stockPriceGama.append({
                'codigo_producto': val.get('codigo_producto'),
                'nombre': val.get('nombre'),
                'gama': val.get('gama'),
                'cantidad_en_stock': val.get('cantidad_en_stock'),
                'precio_venta': val.get('precio_venta')
            })
    stockPriceGama.sort(key=lambda x: x['precio_venta'], reverse=True)
    return stockPriceGama

def menu():
    while True:
     print("""
        ---REPORTES DE LOS PRODUCTOS---
          
          1. Obtener y ordenar los precios de los productos de la gama ornamental de mayor a menor 
          2. Guardar 
         
       Presiona (Ctrl + C) para regresar al menú principal
""")
     try:

      opcion = int(input('Seleccione una de las opciones => '))
      if opcion == 1:
       print(tabulate(getAllStocksPriceGama(), headers = "keys", tablefmt= "fancy_grid"))
      elif opcion == 2:
         producto = {
             'codigo_producto': input('Ingrese el codigo del producto => '),
             'nombre': input('Ingrese el nombre del producto => '),
             'gama': input('Ingrese la gama del producto => '),
             'dimensiones': input('Ingrese las dimensiones del producto => '),
             'proveedor': input('Ingrese el proveedor del producto => '),
             'descripcion': input('Ingrese la descripcion del producto => '),
             'cantidad_en_stock': int(input('Ingrese la cantidad en stock del producto => ')),
             'precio_venta': int(input('Ingrese el precio de venta del producto => ')),
             'precio_proveedor': int(input('Ingrese el precio del producto'))
         }
         psProducto.postProducto(producto)
         print("Producto Guardado")
     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break


