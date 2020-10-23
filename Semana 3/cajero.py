# Modelar un cajero automático

saldo = 1000000

def consultar(saldo_cuenta):
    return saldo_cuenta

def consignar(saldo_cuenta, valor):
    saldo_cuenta = saldo_cuenta + valor
    return saldo_cuenta

def retirar(saldo_cuenta, valor):
    saldo_cuenta -= valor
    return saldo_cuenta

flag = True

while flag:
    print("Bienvenidos a nuestro cajero")
    print("1 - Para consultar saldo")
    print("2 - Para consignar")
    print("3 - Para retirar")
    print("0 - Para salir\n")

    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        print(f"\nSu saldo es: {consultar(saldo)} \n")
    elif opcion == 2:
        valor_consignar = float(input("Valor a consignar: "))
        saldo = consignar(saldo, valor_consignar)
        print(f"\nSu saldo es: {saldo}\n")
    elif opcion == 3:
        valor_retirar = float(input("Valor a retirar: "))
        saldo = retirar(saldo, valor_retirar)
        print(f"\nSu saldo es: {saldo} \n")
    elif opcion == 0:
        print("\nGracias por utilizar nuestro servicio")
        flag = False
    else:
        print("\nOpción no valida")

