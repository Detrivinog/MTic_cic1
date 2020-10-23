"""
Escriba un programa que reciba un año (número entero), verifique que el año sea mayor a 2000 y que sea bisiesto.
"""

year = int(input("Escribe un año: "))

if year > 2000 and year % 4 == 0:
    print("Es un año mayor al 2000 y es bisiesto")
elif year < 2000 and year % 4 == 0:
    print("Es un año menor al 2000 y es bisiesto")
elif year < 2000 and year % 4 != 0:
    print("es un año menor al 2000 y no es bisiesto")
else:
    print("Es un año mayor al 2000 y no es bisiesto")

