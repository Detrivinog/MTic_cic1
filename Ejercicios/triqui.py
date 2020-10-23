tablero = [ x for x in range(1,10,1)]

def mostrar(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[j+3*i], sep = "", end = "  ")
        print("") 

def marcar(posicion, simbolo):
    posicion = int(input("Ingresa la posición a marcar: "))
    marca = ['O', 'X']
    if simbolo == 1:
        tablero[posicion-1] = marca[1]
    else:
        tablero[posicion-1] = marca[0]

def cambio_turno(turno):
    if turno == 1:
        return 0
    return 1    

sistema = True
while sistema:
    print("Bienvenido al juego de triqui by DavidT")
    print("Tienes diferentes formas de juego")
    print("1 - Juega contra otro jugador")
    print("2 - Juega contra la computadora")
    print("3 - Salir del juego")

    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        jugador1 = input("Ingresa el nombre del jugador 1: ")
        jugador2 = input("Ingresa el nombre del jugador 2: ")
        print(f"Empieza {jugador1} con 'O'\n a continuación ")
    elif opcion == 2:
        print("Ya vamos para allá")    
    elif opcion == 3:
        sistema = False
    else: 
        print("La opción no es valida, ingresa un valor del menú")