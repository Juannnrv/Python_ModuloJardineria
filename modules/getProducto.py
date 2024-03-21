import requests
from tabulate import tabulate
import os

def getAllDataProduct():
   # http://154.38.171.54:5008/productos
   peticion = requests.get("http://154.38.171.54:5008/productos")
   data = peticion.json()
   return data

def getProductoCodigo(codigo):
   peticion = requests.get(f"http://154.38.171.54:5008/productos/{codigo}") 

   return [peticion.json()] if peticion.ok else[]

   
def getAllId(id):
   peticion = requests.get(f'http://154.38.171.54:5002/detalle_pedido/{id}')
   if peticion.ok:
      return [peticion.json()]
   else:
      return []

def getAllStocksPriceGama():
    stockPriceGama = []
    for val in getAllDataProduct():
        gama = val.get('gama')
        stock = val.get('cantidadEnStock')
        if gama == 'Ornamentales' and stock >= 100:
            stockPriceGama.append({
                'codigo_producto': val.get('codigo_producto'),
                'nombre': val.get('nombre'),
                'gama': val.get('gama'),
                'cantidadEnStock': val.get('cantidadEnStock'),
                'precio_venta': val.get('precio_venta')
            })
    stockPriceGama.sort(key=lambda x: x['precio_venta'], reverse=True)
    return stockPriceGama

def menu():
    os.system('clear')
    while True:
     print("""
                                   ---REPORTES DE LOS PRODUCTOS---
          
          1. Obtener y ordenar los precios de los productos de la gama ornamental de mayor a menor 
         
                          Presiona (Ctrl + C) para regresar al menú principal
""")
     opcion = int(input('Seleccione una de las opciones => '))
     try:
      
        if opcion == 1:
         print(tabulate(getAllStocksPriceGama(), headers = "keys", tablefmt= 'fancy_grid'))

     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break
    


