""" Realice un programa (script) en Python que calcule y muestre el área de un círculo de radio """

from math import pi

radio = float(input("El radio del circulo es: "))
print("El área del circulo es: ", round(pi*radio**2, 4))

