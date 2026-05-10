import math 

def calcularAreaCirculo(radio):
    area = math.pi * (radio ** 2)
    return area

radio = float(input("ingrese el radio del circulo: "))
area = calcularAreaCirculo(radio)
print(f"el area del circulo es : {area:.2f}")