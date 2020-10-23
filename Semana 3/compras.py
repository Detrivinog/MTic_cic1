"""
El Centro Comercial Unaleño está muy cerca de crear carrito de compras. 
Ahora lo que se requiere de su parte es que se puedan agregar un número indefinido de artículos y calcular la cuenta.
Se han definido varios comandos para realizar la prueba de la lógica del carrito de compras a bajo nivel. 
Para esto se definen ahora diferentes comandos que se realizan al momento de realizar 
una compra y que presentan la siguiente sintaxis: 
comando&sintaxis_comando
Los comandos definidos ahora son:
Comando 1:  Añadir ítem al carrito de compras
La sintaxis del comando 1 es la siguiente:
1&nombre_articulo&cantidad&precio
Comando 2: Generar tirilla de compras
La sintaxis del comando 2 es la siguiente:
2&cedula_cliente
Esta función debe retornar la tirilla de compras en texto
El cálculo de descuento se mantiene y se debe generar la misma tirilla que se generó en el reto anterior, 
pero incluyendo la cédula del cliente y la cantidad de artículos por producto en el formato indicado en el ejemplo.  
Dado el valor total de la compra se continúa con la campaña titulada compra más 
y gasta menos con los siguientes descuentos:
Por compras mayores a 150000 lleva un 10% de descuento.
Por compras mayores a 300000 lleva un 15% de descuento.
Por compras mayores a 700000 lleva un 20% de descuento
Al imprimir la tirilla, la aplicación elimina ese carrito de compras y queda disponible para ejecutar de nuevo comandos.
Comando 3 – Salir de la aplicación
La sintaxis del comando 3 es la siguiente:
3
Este comando simplemente permite salir de la aplicación
Entrada: Diferentes comandos según el cargue y la impresión de tirillas de venta
Salida: Salidas dependiendo del comando especificado anteriormente
"""


def generar_tirilla(produc, cant, prec):
    n = len(cant)
    prod = [None]*n
    for i in range(n):
        prod[i] = cant[i]*prec[i]
    total = sum(prod)
    if total > 150000 and total <= 300000:
        descuento = int(0.1 * total)
    elif total > 300000 and total <= 700000:
        descuento = int(0.15 * total)
    elif total > 700000:
        descuento = int(0.2 * total)
    else:
        descuento = 0
    for i in range(0, n, 1):
        print(produc[i] + " x" + str(cant[i]) + " $" + str(prod[i]))
    print("Total: $" + str(total-descuento))
    print("En esta compra tu descuento fue $" + str(descuento))
    print("Gracias por tu compra\n---")


sistema = True
while sistema:
    producto = []
    cantidad = []
    precio = []
    usuario = True and sistema
    while usuario:
        entrada = input().split('&')
        comando = entrada[0]
        if comando == '1':
            producto.append(entrada[1])
            cantidad.append(int(entrada[2]))
            precio.append(int(entrada[3]))
        elif comando == '2':
            print("Centro Comercial Unaleño\nCompra más y Gasta Menos\nNIT: 899.999.063")
            print("Cliente: " + str(entrada[1]))
            print("Art Cant Precio")
            generar_tirilla(producto, cantidad, precio)
            usuario = False
        elif comando == '3':
            usuario = False
            sistema = False




        
    