"""
Dado un número entero n y otro entero m, escriba un programa que muestre los múltiplos de m hasta n.

Entrada
Los números n y m. Para este laboratorio es necesario que al leer n y m agrege los mensajes "digite n:" y "digite m:"
Salida
Como salida se debe mostrar el aviso
"""

n = int(input("digite n: "))
m = int(input("digite m: "))

print("Los múltiplos son:")
for i in range(0, n+1, m):
    print(i)