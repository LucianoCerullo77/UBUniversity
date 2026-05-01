cantPares = 0
cantImpares = 0

terminacion = int(input("ingrese terminacion de patente (0-9), -1 para terminar: "))

while terminacion != -1:
    # valido que este entre 0 y 9
    if terminacion >= 0 and terminacion <= 9:
        if terminacion % 2 == 0:
            cantPares = cantPares + 1
        else:
            cantImpares = cantImpares + 1
    else:
        print("valor invalido, ingrese entre 0 y 9")

    terminacion = int(input("ingrese terminacion de patente (0-9), -1 para terminar: "))

print("vehiculos con numeracion par:", cantPares)
print("vehiculos con numeracion impar:", cantImpares)