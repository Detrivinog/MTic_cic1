"""
A partir del día 1, el país A tiene una población contagiada de Divoc 9012 de n (1 <=n <= 10^8) 
y el país B tiene una población contagiada de Divoc 9012 de m (1 <= m <= n). 
Las tasas de crecimiento diario son de 2% y 3% respectivamente. Desarrollar un algoritmo 
para informar en que día la población contagiada del país B iguala o supera a la del país A.

Entrada
La entrada consta de dos números reales que representan la cantidad de gente contagiada.

Salida
El día en el cual la población contagiada del país B supera la del país A
"""

n = int(input())
m = int(input())

dias = 1
while n > m:
    n = n * 1.02
    m = m * 1.03
    dias += 1

print(dias)