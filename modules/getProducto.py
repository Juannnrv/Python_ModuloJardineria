import storage.producto as pr
from tabulate import tabulate

def getAllStocksPriceGama():
    stockPriceGama = []
    for val in pr.producto:
        gama = val.get('gama')
        stock = val.get('cantidad_en_stock')
        if gama == 'Ornamentales' and stock >= 100:
            stockPriceGama.append({
                'codigo_producto': val.get('codigo_producto'),
                'nombre': val.get('nombre'),
                'gama': val.get('gama'),
                'cantidad_en_stock': val.get('cantidad_en_stock'),
                'precio_venta': val.get('precio_venta')
            })
            stockPriceGama.sort(key=lambda x: x['precio_venta'], reverse = True)
    return stockPriceGama


def menu():
    print(tabulate(getAllStocksPriceGama(), headers = "keys", tablefmt= "fancy_grid"))
    


