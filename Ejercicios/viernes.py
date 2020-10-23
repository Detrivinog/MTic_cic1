"""
Escriba un programa que reciba del usuario que día de la semana es, el programa debe
imprimir cuántos días faltan para el viernes.
"""

dias = ["lunes", "martes", "miercóles", "jueves", "viernes", "sábado", "domingo"]
hoy = input('Qúe día es hoy: ')
i = dias.index(hoy)
j = 0
while i != 4:
  j += 1
  i += 1
  if i > 6:
    i = 0

print(f"Faltan {j} días para el viernes")



