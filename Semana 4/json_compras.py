"""
Reto 4: Generar tirilla de compras a partir de un archivo JSON
"""
def ordenar_productos(lista_productos):
    n = len(lista_productos)
    productos = [None]*n
    cantidad = [None]*n
    precio = [None]*n
    for i in range(n):
        productos[i] = lista_productos[i]['nombre']
        cantidad[i] = int(lista_productos[i]['cantidad'])
        precio[i] = int(lista_productos[i]['precio unitario'])
    return [productos, cantidad, precio]

def generar_tirilla(produc, cant, prec):
    n = len(cant)
    prod = [None]*n
    for i in range(n):
        prod[i] = cant[i]*prec[i]
    total = sum(prod)
    if total > 150000 and total <= 300000:
        descuento = int(0.1 * total)
    elif total > 300000 and total <= 700000:
        descuento = int(0.15 * total)
    elif total > 700000:
        descuento = int(0.2 * total)
    else:
        descuento = 0
    for i in range(0, n, 1):
        print(produc[i] + " x" + str(cant[i]) + " $" + str(prod[i]))
    print("Total: $" + str(total-descuento))
    print("En esta compra tu descuento fue $" + str(descuento))
    print("Gracias por tu compra\n---")

import json
import requests
from pprint import pprint

jtirilla = requests.get(input())
tirilla = json.loads(jtirilla.text)
print(tirilla[0]['productos'][0]['nombre'])
print(len(tirilla))
print(type(tirilla[0]['productos'][0]))
n = len(tirilla)
for i in range(n):
    usuario = tirilla[i]['cliente']
    lista_productos = tirilla[i]['productos']
    print("Centro Comercial Unaleño\nCompra más y Gasta Menos\nNIT: 899.999.063")
    print("Cliente: " + str(usuario))
    print("Art Cant Precio")
    ordenados = ordenar_productos(lista_productos)
    generar_tirilla(ordenados[0], ordenados[1], ordenados[2])

