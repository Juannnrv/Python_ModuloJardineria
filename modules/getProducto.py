import storage.producto as pr
from tabulate import tabulate

def getAllStocksPriceGama():
    stockPriceGama = []
    for val in pr.producto:
        gama = val.get('gama')
        stock = val.get('cantidad_en_stock')
        descripcion = val.get('descripcion')
        if gama == 'Ornamentales' and stock >= 100 and descripcion is not None:
            descripcion_cortada = descripcion[:10] if descripcion else None
            stockPriceGama.append({
                'codigo_producto': val.get('codigo_producto'),
                'nombre': val.get('nombre'),
                'gama': val.get('gama'),
                'descripcion': descripcion_cortada,  
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
          2. Obtener  
         
       Presiona (Ctrl + C) para regresar al menú principal
""")
     try:

      opcion = int(input('Seleccione una de las opciones => '))
      if opcion == 1:
       print(tabulate(getAllStocksPriceGama(), headers = "keys", tablefmt= "fancy_grid"))
     except KeyboardInterrupt:
         print()
         print()
         print('SALIENDO...')
         break


