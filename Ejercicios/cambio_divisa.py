"""
Desarrolle un programa que convierta de una moneda extranjera a pesos colombianos. 
El usuario debe ingresar, el nombre de la moneda extranjera, la cantidad de dinero 
que desea convertir y la tasa de cambio actual (1 peso colombiano es equivalente a 
cuantos en la moneda extranjera). El resultado del programa debe ser la cantidad de pesos colombianos.
"""

moneda_extranjera = input("La moneda extranjera es: ")
cantidad = int(input("Cantidad a cambiar: "))
tasa = float(input(f"La tasa de cambio de {moneda_extranjera} a pesos colombianos es: "))
pesos = cantidad * tasa

print(f"{cantidad} {moneda_extranjera} equivalen a {pesos} pesos colombianos")

