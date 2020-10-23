n = int(input())
i = 0
producto = [None]*n
precio = [None]*n
while i < n:
    producto[i]=input()
    precio[i]=int(input())
    i += 1

total = sum(precio)
if total > 150000 and total <= 300000:
    descuento = int(0.1 * total)
elif total > 300000 and total <= 700000:
    descuento = int(0.15 * total)
elif total > 700000:
    descuento = int(0.2 * total)
else:
    descuento = 0
 
print("Centro Comercial Unaleño\nCompra más y Gasta Menos\nNIT: 899.999.063")
for i in range(0, n, 1):
    print(producto[i] + " $ "+ str(precio[i]))
print("Total: $" + str(total-descuento))
print("En esta compra tu descuento fue $" + str(descuento))
print("Gracias por tu compra")
