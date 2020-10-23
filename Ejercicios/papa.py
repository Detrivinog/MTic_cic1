"""
Realice un programa (script) en Python calcule el PAPA (Promedio Aritmético Ponderado Acumulado ) 
de un estudiante que terminó su primer semestre y cursó cuatro asignaturas.
El programa debe recibir del usuario el número de créditos y la nota final 
por cada una de las cuatro asignaturas y mostrar el PAPA resultante.
"""

i = 0
creditos = [None]*4
notas = [None]*4
while i < 4:
    creditos[i] = int(input(f"Número de creditos de la materia {i+1}: "))
    notas[i] = float(input(f"La nota fue de la materia {i+1} fue: "))
    i += 1

papa = 0
for i in range(4):
    papa = papa + creditos[i] * notas[i]

print(f"El PAPA fue de: {round(papa/sum(creditos), 3)}")