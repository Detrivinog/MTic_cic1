from math import pi

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
r1 = float(input())
r2 = float(input())

def area_total(a1,b1,a2,b2,r1,r2): 
    def area_rectangulo(a,b):
        return a*b
    
    def area_circulo(r):
        return pi*r*r
    
    total = area_rectangulo(a1,b1) + area_rectangulo(a2,b2) + area_circulo(r1) + area_circulo(r2)
    return total

print("suma total =", area_total(a1,b1,a2,b2,r1,r2))