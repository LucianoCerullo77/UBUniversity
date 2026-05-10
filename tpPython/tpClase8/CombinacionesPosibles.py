import math

def calcularCombinaciones(miLista):
    return math.factorial(len(miLista))

fichas = input("Ingrese las fichas, separadas por coma. ej: A,B,C: ").split(",")
## con esto limpio los espacios en blanco del usuario
fichas = [letra.strip() for letra in fichas]

resultado = calcularCombinaciones(fichas)
print(f"cantidad de combinaciones posibles? : {resultado}")
