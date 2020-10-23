"""
Utilizando tuplas elabore un método que retorne la distancia 
entre dos puntos 𝑝 y 𝑞 definidos en un espacio de 3 dimensiones:
La distancia corresponde a aplicar: distancia euclidiana
Entrada
La entrada corresponde a los valores de cada una de las coordenadas x, y, z de cada punto:
Salida
Un único valor correspondiente a la distancia entre los dos puntos.
Para una mayor referencia puede consultar distancias en el espacio
"""
from math import sqrt

p = tuple(map(int, input().split(' ')))
q = tuple(map(int, input().split(' ')))

def distancia(a,b):
    d = [None]*len(a)
    for i in range(len(a)):
        d[i] = (a[i]-b[i])**2

    return sqrt(sum(d))

print(distancia(p,q))